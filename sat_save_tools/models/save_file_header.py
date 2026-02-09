import datetime
import enum
import logging
import typing

import pydantic

from sat_save_tools.const import (
    EPOCH_1_TO_1970,
    SUPPORT_HEADER_TYPES,
    SUPPORT_SAVE_VERSIONS,
    TICKS_IN_SECOND,
)
from sat_save_tools.exceptions import SatisfactorySaveParserError
from sat_save_tools.serde import (
    U32,
    U64,
    B64Raw,
    Deserializer,
    Object,
    Raw,
    String,
    U32Bool,
)
from sat_save_tools.utils import (
    U8EnumDeserializerMixin,
    U8EnumSerializerMixin,
    pydantic_eq,
)

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Serializer

__all__ = ("SaveFileHeader", "SaveFileHeaderFlags")

logger = logging.getLogger()


class SaveFileHeaderFlags(U8EnumSerializerMixin, U8EnumDeserializerMixin, enum.IntFlag):
    FRIENDS_ONLY = 1 << 0  # 0 = public, 1 = friends only
    RESERVED_1 = 1 << 1
    RESERVED_2 = 1 << 2
    UNKNOWN_3 = 1 << 3
    UNKNOWN_4 = 1 << 4
    UNKNOWN_5 = 1 << 5
    UNKNOWN_6 = 1 << 6
    UNKNOWN_7 = 1 << 7


@pydantic_eq
class SaveFileHeader(pydantic.BaseModel):
    header_version: typing.Annotated[
        int,
        pydantic.Field(
            title="save header version",
            description="for a version list see the header FGSaveManagerInterface.h in the https://satisfactory.wiki.gg/wiki/Community_resources",
        ),
    ]
    save_version: typing.Annotated[
        int,
        pydantic.Field(
            title="save version",
            description="for a version list see the header SaveCustomVersion.h in the https://satisfactory.wiki.gg/wiki/Community_resources",
        ),
    ]
    build_version: typing.Annotated[int, pydantic.Field(title="build version")]
    save_name: typing.Annotated[str, pydantic.Field(title="save name")]
    map_name: str
    map_options: str
    session_name: str
    play_duration: int
    save_ticks: int
    flags: SaveFileHeaderFlags
    editor_object_version: typing.Annotated[
        int | None,
        pydantic.Field(description="depends on the unreal engine version used"),
    ] = None
    mod_metadata: str | None = None
    mod_flags: int | None = None
    save_id: str | None = None
    is_partitioned_world: bool | None = None
    creative_mode_enabled: bool | None = None
    checksum: pydantic.Base64Bytes | None = None
    is_cheat: bool | None = None

    @staticmethod
    def raise_if_none[T](t: T | None) -> T:
        if t is None:
            raise SatisfactorySaveParserError("corrupt_data", "Value in header is None. May be other version?")
        return t

    @property
    def play_timedelta(self) -> datetime.timedelta | None:
        return datetime.timedelta(seconds=self.play_duration)

    @property
    def save_datetime(self) -> datetime.datetime | None:
        return datetime.datetime.fromtimestamp(self.save_ticks / TICKS_IN_SECOND - EPOCH_1_TO_1970)

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(self.header_version) | U32(self.save_version) | U32(self.build_version))

        if self.header_version >= 14:
            ser.add_struct(String(self.save_name))

        ser.add_struct(
            String(self.map_name)
            | String(self.map_options)
            | String(self.session_name)
            | U32(self.play_duration)
            | U64(self.save_ticks)
            | Object(self.flags),
        )
        if self.header_version >= 7:
            ser.add_struct(U32(self.raise_if_none(self.editor_object_version)))
        if self.header_version >= 8:
            ser.add_struct(String(self.raise_if_none(self.mod_metadata)) | U32(self.raise_if_none(self.mod_flags)))
        if self.header_version >= 10:
            ser.add_struct(String(self.save_id))
        if self.header_version >= 13:
            ser.add_struct(
                U32Bool(self.raise_if_none(self.is_partitioned_world))
                | U32Bool(self.raise_if_none(self.creative_mode_enabled))
                | Raw(len(self.raise_if_none(self.checksum)))(self.raise_if_none(self.checksum))
                | U32Bool(self.raise_if_none(self.is_cheat)),
            )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("header_version"))
        if content["header_version"] not in SUPPORT_HEADER_TYPES:
            raise SatisfactorySaveParserError(
                "unsupported_version",
                "Unsupported save header version number {}",
                content["header_version"],
            )
        content |= des.get_dict(U32("save_version") | U32("build_version"))
        if content["save_version"] not in SUPPORT_SAVE_VERSIONS:
            raise SatisfactorySaveParserError(
                "unsupported_version",
                "Unsupported save version number {}",
                content["save_version"],
            )

        if content["header_version"] >= 14:
            content |= des.get_dict(String("save_name"))

        content |= des.get_dict(
            String("map_name")
            | String("map_options")
            | String("session_name")
            | U32("play_duration")
            | U64("save_ticks")
            | Object(SaveFileHeaderFlags)("flags"),
        )

        if content["header_version"] >= 7:
            content |= des.get_dict(U32("editor_object_version"))
        if content["header_version"] >= 8:
            content |= des.get_dict(String("mod_metadata") | U32("mod_flags"))
        if content["header_version"] >= 10:
            content |= des.get_dict(String("save_id"))
        if content["header_version"] >= 13:
            content |= des.get_dict(
                U32Bool("is_partitioned_world")
                | U32Bool("creative_mode_enabled")
                | B64Raw(16)("checksum")
                | U32Bool("is_cheat"),
            )

        return cls.model_validate(content)
