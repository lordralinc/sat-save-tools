import logging
import typing

import pydantic

from sat_save_tools.data import ConstDataView
from sat_save_tools.dev import dev_dump_unparsed_chunk
from sat_save_tools.logger import set_struct_name
from sat_save_tools.models.object_header import ActorHeader, ComponentHeader, HeaderType
from sat_save_tools.models.object_reference import ObjectReference
from sat_save_tools.models.properties import PropertyList
from sat_save_tools.serde import U32, Float, Object, Raw, String, Struct
from sat_save_tools.utils import b64_bytes, expect_size, float_eq, pydantic_eq

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializer

__all__ = (
    "ActorObject",
    "BlueprintGameModeTrailingContainer",
    "ComponentObject",
    "ConveyorTrailing",
    "ConveyorTrailingContainer",
    "LevelObjectType",
)

logger = logging.getLogger(__name__)


@float_eq(
    float_slots=("postition",),
    other_slots=(
        "length",
        "name",
        "unk1",
        "unk2",
    ),
)
class ConveyorTrailing(pydantic.BaseModel):
    length: int
    name: str
    unk1: str
    unk2: str
    postition: float

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(self.length) | String(self.name) | String(self.unk1) | String(self.unk2) | Float(self.postition),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                U32("length") | String("name") | String("unk1") | String("unk2") | Float("postition"),
            ),
        )


@pydantic_eq
class ConveyorTrailingContainer(pydantic.BaseModel):
    items: list[ConveyorTrailing]

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        count = des.get_struct(U32)[0]
        content = {"items": des.get_struct(Object(ConveyorTrailing) * count)}
        return cls.model_validate(content)

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(len(self.items)) | Struct.from_iter(Object, self.items))


@pydantic_eq
class BlueprintGameModeTrailingContainer(pydantic.BaseModel):
    __target_type_paths__: typing.ClassVar[tuple[str, ...]] = (
        "/Game/FactoryGame/-Shared/Blueprint/BP_GameMode.BP_GameMode_C",
        "/Game/FactoryGame/-Shared/Blueprint/BP_GameState.BP_GameState_C",
    )
    items: list[ObjectReference]

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        count = des.get_struct(U32)[0]
        content = {"items": des.get_struct(Object(ObjectReference) * count)}
        return cls.model_validate(content)

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(len(self.items)) | Struct.from_iter(Object, self.items))


@pydantic_eq
class PowerLineTrailingContainer(pydantic.BaseModel):
    __target_type_paths__: typing.ClassVar[tuple[str, ...]] = (
        "/Game/FactoryGame/Buildable/Factory/PowerLine/Build_PowerLine.Build_PowerLine_C",
    )
    items: tuple[ObjectReference, ObjectReference]

    def __serialize__(self, ser: "Serializer") -> None:
        for it in self.items:
            ser.add(it)

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls(items=(des.get(ObjectReference), des.get(ObjectReference)))


type ActorObjectTrailingType = (
    ConveyorTrailingContainer | BlueprintGameModeTrailingContainer | PowerLineTrailingContainer
)


@set_struct_name("ActorObjectTrailing")
def deserialize_actor_object_trailing(
    des: "Deserializer",
    header: ActorHeader,
    size: int,
) -> ActorObjectTrailingType | pydantic.Base64Bytes:
    if header.type_path in ConstDataView().conveyor_belts:
        return des.get(ConveyorTrailingContainer)

    for trailing_container_cls in [
        BlueprintGameModeTrailingContainer,
        PowerLineTrailingContainer,
    ]:
        if header.type_path in trailing_container_cls.__target_type_paths__:
            return des.get(trailing_container_cls)
    content = des.get_raw(size)
    dev_dump_unparsed_chunk(
        "actor_trailing",
        header.type_path,
        header.instance_name,
        content=content,
    )
    if logger.isEnabledFor(logging.WARNING):
        logger.warning(
            "No deserializer found for %r instance_name: %r",
            header.type_path,
            header.instance_name,
        )
    return content


@pydantic_eq
class ActorObject(pydantic.BaseModel):
    type: typing.Literal[HeaderType.ACTOR] = HeaderType.ACTOR
    header: ActorHeader
    save_version: int
    flag: int
    parent_object_reference: ObjectReference
    components: list[ObjectReference]
    properties: PropertyList
    trailing: ActorObjectTrailingType | pydantic.Base64Bytes

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(
            Object(self.parent_object_reference)
            | U32(len(self.components))
            | Struct.from_iter(Object, self.components)
            | Object(self.properties)
            | U32(0),
        )
        if self.trailing is not None:
            if isinstance(self.trailing, (bytes, bytearray, memoryview)):
                ns.add_raw(self.trailing)
            else:
                ns.add(self.trailing)
        ser.add_struct(U32(self.save_version) | U32(self.flag) | U32(len(ns)))
        ser.add(ns)

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        header: "ActorHeader" = des.ctx_get("level_object_header")

        content = des.get_dict(U32("save_version") | U32("flag") | U32("size")) | {
            "header": header,
        }

        with expect_size(des, content["size"], "ActorObject"):
            start_offset = des.offset
            content |= des.get_dict(Object(ObjectReference)("parent_object_reference") | U32("components_size"))
            content["components"] = des.get_struct(Object(ObjectReference) * content["components_size"])
            content |= des.get_dict(Object(PropertyList)("properties") | U32("unknown"))
            remaining_size = content["size"] - (des.offset - start_offset)
            if remaining_size > 0:
                content["trailing"] = b64_bytes(des.get_raw(remaining_size))
            else:
                content["trailing"] = b64_bytes(b"")
        return cls.model_validate(content)


@pydantic_eq
class ComponentObject(pydantic.BaseModel):
    type: typing.Literal[HeaderType.COMPONENT] = HeaderType.COMPONENT
    header: ComponentHeader
    save_version: int
    flag: int
    properties: PropertyList
    trailing: pydantic.Base64Bytes

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(Object(self.properties) | U32(0))
        if self.trailing is not None:
            ns.add_struct(Raw(len(self.trailing))(self.trailing))
        ser.add_struct(U32(self.save_version) | U32(self.flag) | U32(len(ns)) | Raw(len(ns))(ns.content))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        header: "ComponentHeader" = des.ctx_get("level_object_header")

        content = des.get_dict(
            U32("save_version") | U32("flag") | U32("size"),
        ) | {"header": header}
        with expect_size(des, content["size"], "ComponentObject"):
            start_offset = des.offset
            content |= des.get_dict(Object(PropertyList)("properties") | U32("unknown"))
            trailing_size = content["size"] - (des.offset - start_offset)
            if trailing_size > 0:
                content["trailing"] = b64_bytes(des.get_raw(trailing_size))
            else:
                content["trailing"] = b64_bytes(b"")
        return cls.model_validate(content)


type LevelObjectType = typing.Annotated[ActorObject | ComponentObject, pydantic.Field(discriminator="type")]
