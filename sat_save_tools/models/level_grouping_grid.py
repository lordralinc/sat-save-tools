import enum
import typing

import pydantic

from sat_save_tools.serde import U32, Object, String, Struct
from sat_save_tools.utils import (
    StrEnumDeserializerMixin,
    StrEnumSerializerMixin,
    pydantic_eq,
)

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializer

__all__ = (
    "GridName",
    "LevelGroupingGrid",
    "LevelInfo",
)


class GridName(StrEnumSerializerMixin, StrEnumDeserializerMixin, enum.StrEnum):
    MAIN = "MainGrid"
    LANDSCAPE = "LandscapeGrid"
    EXPLORATION = "ExplorationGrid"
    FOLIAGE = "FoliageGrid"
    HLOD = "HLOD0_256m_1023m"


@pydantic_eq
class LevelInfo(pydantic.BaseModel):
    name: typing.Annotated[str, pydantic.Field(title="Level Name", description="Name of the sublevel")]
    value: typing.Annotated[
        int,
        pydantic.Field(title="Level Value", description="Associated integer for the level"),
    ]

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(String(self.name) | U32(self.value))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(des.get_dict(String("name") | U32("value")))


@pydantic_eq
class LevelGroupingGrid(pydantic.BaseModel):
    name: typing.Annotated[GridName, pydantic.Field(title="Grid Name")]
    hex: typing.Annotated[int, pydantic.Field(title="Unknown Uint32 #1", description="Purpose unclear")]
    count: typing.Annotated[int, pydantic.Field(title="Unknown Uint32 #2", description="Purpose unclear")]
    levels: typing.Annotated[
        list[LevelInfo],
        pydantic.Field(title="Level Info", description="List of level name + integer pairs"),
    ]

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            Object(self.name)
            | U32(self.hex)
            | U32(self.count)
            | U32(len(self.levels))
            | Struct.from_iter(Object, self.levels),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            Object(GridName)("name") | U32("hex") | U32("count") | U32("levels_count"),
        )
        content["levels"] = des.get_struct(Object(LevelInfo) * content["levels_count"])
        return cls.model_validate(content)
