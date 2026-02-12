import itertools
import logging
import typing
from functools import reduce

import pydantic

from sat_save_tools.progress import LogProgress
from sat_save_tools.serde import U32, U64, Object, String
from sat_save_tools.utils import pydantic_eq

if typing.TYPE_CHECKING:
    from sat_save_tools.models import SaveFileHeader
    from sat_save_tools.models.level import Level
    from sat_save_tools.models.level_grouping_grid import LevelGroupingGrid
    from sat_save_tools.serde import Deserializer, Serializer

__all__ = ("SaveFileBody",)

logger = logging.getLogger(__name__)


@pydantic_eq
class SaveFileBody(pydantic.BaseModel):
    partition_count: int
    hex_1: int
    hex_2: int
    grids: typing.Annotated[list["LevelGroupingGrid"], pydantic.Field(min_length=5, max_length=5)]
    levels: list["Level"]
    persistent_level: "Level"

    @property
    def full_levels(self) -> "list[Level]":
        return [*self.levels, self.persistent_level]

    def __serialize__(self, ser: "Serializer") -> None:
        header: "SaveFileHeader" = ser.ctx_get("header")
        ns = ser.new()
        if header.save_version >= 41 and header.is_partitioned_world:
            ns.add_struct(
                U32(self.partition_count)
                | String("None")
                | U32(0)
                | U32(self.hex_1)
                | U32(1)
                | String("None")
                | U32(self.hex_2)
                | reduce(lambda a, b: a | b, [Object(it) for it in self.grids]),
            )

        ns.add_struct(U32(len(self.levels)))
        for lvl in LogProgress.iter(
            itertools.chain(self.levels, [self.persistent_level]),
            total=len(self.levels) + 1,
            desc="serialize levels",
        ):
            ns.add(lvl)

        ser.add_struct((U64 if header.save_version >= 41 else U32)(len(ns)))
        ser.add(ns)

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        from sat_save_tools.models.level import Level  # noqa: PLC0415
        from sat_save_tools.models.level_grouping_grid import (  # noqa: PLC0415
            LevelGroupingGrid,
        )

        header: "SaveFileHeader" = des.ctx_get("header")
        content = des.get_dict((U64 if header.save_version >= 41 else U32)("uncompressed_size"))

        if header.save_version >= 41 and header.is_partitioned_world:
            content |= des.get_dict(
                U32("partition_count")
                | String("unknown")
                | U32("unkwnown")
                | U32("hex_1")
                | U32("unkwnown")
                | String("unknown")
                | U32("hex_2"),
            )
            content |= {"grids": list(des.get_struct(Object(LevelGroupingGrid) * 5))}

        content |= des.get_dict(U32("sublevel_count"))
        content["levels"] = LogProgress.iter_list(
            [
                des.ctx_update(is_persistent=False).get(Level)
                for _ in LogProgress.iter(
                    range(content["sublevel_count"]),
                    total=content["sublevel_count"],
                    desc="deserialize levels",
                )
            ],
            total=content["sublevel_count"],
            desc="sublevels",
        )
        content["persistent_level"] = des.ctx_update(is_persistent=True).get(Level)

        return cls.model_validate(content)
