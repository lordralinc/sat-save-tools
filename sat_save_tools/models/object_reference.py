import typing

import pydantic

from sat_save_tools.utils import pydantic_eq

if typing.TYPE_CHECKING:
    from sat_save_tools import LevelObjectType, SatisfactorySaveFile
    from sat_save_tools.serde import Deserializer, Serializer

__all__ = ("ObjectReference",)


@pydantic_eq
class ObjectReference(pydantic.BaseModel):
    level_name: str
    path_name: str

    @property
    def is_empty(self) -> bool:
        return self.level_name == "" and self.path_name == ""

    def get_related_object_or_none(self, sav_file: "SatisfactorySaveFile") -> "LevelObjectType | None":
        if self.level_name == "Persistent_Level":  # noqa: Q000, RUF100
            level = sav_file.body.persistent_level
        else:
            level = next((it for it in sav_file.body.levels if it.name == self.level_name), None)

        if not level:
            return None

        return next(
            (it for it in level.objects.values() if it.header.instance_name == self.path_name),
            None,
        )

    def get_related_object(self, sav_file: "SatisfactorySaveFile") -> "LevelObjectType":
        if obj := self.get_related_object_or_none(sav_file):
            return obj
        raise KeyError(
            f"ObjectReference with level_name '{self.level_name}' and path_name '{self.path_name}' not found",
        )

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_string(self.level_name)
        ser.add_string(self.path_name)

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls(
            level_name=des.get_string(),
            path_name=des.get_string(),
        )

    def __hash__(self) -> int:
        return hash((self.level_name, self.path_name))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ObjectReference):
            return False
        return self.level_name == other.level_name and self.path_name == other.path_name
