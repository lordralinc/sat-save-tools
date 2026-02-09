import typing

import pydantic

from sat_save_tools.models.level_objects import (
    ActorObject,
    ComponentObject,
    HeaderType,
    LevelObjectType,
)
from sat_save_tools.models.object_header import deserialize_object_header
from sat_save_tools.models.object_reference import ObjectReference
from sat_save_tools.progress import LogProgress
from sat_save_tools.serde import U32, U64, Function, Object, Raw, String, Struct, U32Bool
from sat_save_tools.utils import pydantic_eq, require

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializer

__all__ = ("Level",)


@pydantic_eq
class Level(pydantic.BaseModel):
    name: str | None = None
    extra_level_name: str | None = None
    collectables: list[ObjectReference] | None = None
    objects: dict[str, LevelObjectType]
    save_version: int | None = None
    second_collectables: list[ObjectReference] | None = None

    def __serialize__(self, ser: "Serializer") -> None:
        is_persistent = self.name is None

        if not is_persistent:
            ser.add_struct(String(require(self.name)))

        object_headers_and_collectables_ser = ser.new()
        object_headers_and_collectables_ser.add_struct(U32(len(self.objects)))
        for obj in LogProgress.iter(
            self.objects.values(),
            total=len(self.objects),
            desc="serialize object headers",
        ):
            object_headers_and_collectables_ser.add(obj.header)

        if is_persistent:
            object_headers_and_collectables_ser.add_struct(
                U32Bool(self.extra_level_name is not None),
            )
            if self.extra_level_name is not None:
                object_headers_and_collectables_ser.add_struct(String(require(self.extra_level_name)))
        if self.collectables is not None:
            object_headers_and_collectables_ser.add_struct(U32(len(require(self.collectables))))
            for collectable in LogProgress.iter(
                self.collectables,
                total=len(self.collectables),
                desc="serialize collectables",
            ):
                object_headers_and_collectables_ser.add(collectable)

        ser.add_struct(
            U64(len(object_headers_and_collectables_ser))
            | Raw(len(object_headers_and_collectables_ser))(object_headers_and_collectables_ser.content),
        )

        objects_ser = ser.new()
        objects_ser.add_struct(U32(len(self.objects)))
        for obj in LogProgress.iter(
            self.objects.values(),
            total=len(self.objects),
            desc="serialize objects",
        ):
            objects_ser.add(obj)
        ser.add_struct(
            U64(len(objects_ser)) | Raw(len(objects_ser))(objects_ser.content),
        )

        if not is_persistent:
            ser.add_struct(U32(require(self.save_version)))
        if self.second_collectables is not None:
            ser.add_struct(
                U32(len(self.second_collectables)) | Struct.from_iter(Object, self.second_collectables),
            )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        is_persistent: bool = des.ctx_get("is_persistent")

        content: dict[str, typing.Any] = {"object_headers": []}
        if not is_persistent:
            content |= des.get_dict(String("name"))

        content |= des.get_dict(U64("object_headers_and_collectables_size"))
        with des.slice(content["object_headers_and_collectables_size"]) as sub_des:
            content |= sub_des.get_dict(U32("object_headers_count"))
            content["object_headers"] = []
            for _ in LogProgress.iter(
                range(content["object_headers_count"]),
                total=content["object_headers_count"],
                desc="deserialize object headers",
            ):
                header = sub_des.get_struct(Function(deserialize_object_header), first=True)
                content["object_headers"].append(header)
            if is_persistent:
                content |= sub_des.get_dict(U32Bool("has_extra_level_name"))
                if content["has_extra_level_name"]:
                    content |= sub_des.get_dict(String("extra_level_name"))
            if sub_des.total != sub_des.offset:
                content["collectables"] = []
                content |= sub_des.get_dict(U32("collectables_count"))
                for _ in LogProgress.iter(
                    range(content["collectables_count"]),
                    total=content["collectables_count"],
                    desc="deserialize collectables",
                ):
                    content["collectables"].append(
                        sub_des.get_struct(
                            Object(ObjectReference)("collectables"),
                            first=True,
                        ),
                    )

        content |= des.get_dict(U64("objects_size"))
        with des.slice(content["objects_size"]) as sub_des:
            content |= sub_des.get_dict(U32("objects_count"))
            content["objects"] = [
                sub_des.ctx_update(level_object_header=content["object_headers"][idx]).get(
                    (ActorObject if content["object_headers"][idx].type == HeaderType.ACTOR else ComponentObject),
                )
                for idx in LogProgress.iter(
                    range(content["objects_count"]),
                    total=content["objects_count"],
                    desc="deserialize level objects",
                )
            ]
            content["objects"] = {it.header.instance_name: it for it in content["objects"]}
        if not is_persistent:
            content |= des.get_dict(U32("save_version"))
        # NOTE: i don’t fully understand how it’s determined whether second_collectables exist
        # NOTE:
        # NOTE: The wiki states:
        # NOTE: - **second collectables count**
        # NOTE: → the number of collectables in the second list that follows.
        # NOTE:     Can be ignored, since the collectables should be exactly the same as above.
        # NOTE:
        # NOTE: - **second collectables**
        # NOTE: → a list of object references.
        # NOTE:     For the format of one `ObjectReference`, see below.
        # NOTE:     Can also be ignored.
        # NOTE:
        # NOTE: SCIM implementation
        # NOTE: ```js
        # NOTE: let countCollected = this.readInt();
        # NOTE: if(countCollected > 0)
        # NOTE: {
        # NOTE:     if(levelName === 'Level ' + this.header.mapName)
        # NOTE:     {
        # NOTE:         this.readString(); // Persistent_Level
        # NOTE:         countCollected = this.readInt();                                # noqa: ERA001
        # NOTE:     }
        # NOTE:
        # NOTE:     for(let i = 0; i < countCollected; i++)
        # NOTE:     {
        # NOTE:       let collectable = this.readObjectProperty();
        # NOTE:        // console.log(2, collectable);
        # NOTE:        collectables.push(collectable);                                  # noqa: ERA001
        # NOTE:     }
        # NOTE: }
        # NOTE: ```
        # NOTE: The second collectables list is only parsed if countCollected > 0.
        # NOTE: For the persistent level (Level <mapName>),
        # NOTE:     an extra string (Persistent_Level) is read before the actual count.
        # NOTE: Parsed collectables are appended to the same collectables array.

        # NOTE: sav_parse.py implementation
        # NOTE: if not persistentLevelFlag:
        # NOTE: (offset, collectedCount2) = parseUint32(offset, data)                   # noqa: ERA001
        # NOTE: for count in range(collectedCount2):
        # NOTE:     (offset, objectReference) = parseObjectReference(offset, data)      # noqa: ERA001
        # NOTE:     collectables2.append(objectReference)                               # noqa: ERA001
        # NOTE:
        # NOTE: The second collectables list is skipped entirely when persistentLevelFlag is set.
        # NOTE: Otherwise, the count is read unconditionally.
        # NOTE: Object references are stored separately in collectables2.
        if not content.get("has_extra_level_name"):
            content["second_collectables"] = []
            content |= des.get_dict(U32("second_collectables_count"))
            for _ in LogProgress.iter(
                range(content["second_collectables_count"]),
                total=content["second_collectables_count"],
                desc="deseriaize second collectables",
            ):
                content["second_collectables"].append(des.get_struct(Object(ObjectReference), first=True))
        return cls.model_validate(content)
