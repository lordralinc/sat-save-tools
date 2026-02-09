import collections
import collections.abc
import enum
import logging
import typing
import uuid

import pydantic

from sat_save_tools.logger import set_struct_name
from sat_save_tools.models.object_reference import ObjectReference
from sat_save_tools.models.properties.enums import StructTypeName
from sat_save_tools.serde import (
    I64,
    U8,
    U32,
    B64Raw,
    Double,
    Float,
    Object,
    Raw,
    String,
    Struct,
    U8Bool,
    U32Bool,
)
from sat_save_tools.utils import (
    SatisfactorySaveParserError,
    U8EnumDeserializerMixin,
    U8EnumSerializerMixin,
    b64_bytes,
    float_eq,
    pydantic_eq,
)

if typing.TYPE_CHECKING:
    from sat_save_tools.models.properties import PropertyList
    from sat_save_tools.serde import Deserializer, Serializer


__all__ = (
    "Box",
    "ClientIdentityInfo",
    "ClientIdentityInfoIdentity",
    "ClientIdentityInfoIdentityVariant",
    "DateTime",
    "DoubleQuaternion",
    "DoubleVector3",
    "FloatQuaternion",
    "FloatVector3",
    "FluidBox",
    "InventoryItem",
    "LinearColor",
    "RailroadTrackPosition",
    "SpawnData",
)

logger = logging.getLogger(__name__)


@float_eq(
    double_slots=(
        "min_x",
        "min_y",
        "min_z",
        "max_x",
        "max_y",
        "max_z",
    ),
    other_slots=("is_valid",),
)
class Box(pydantic.BaseModel):
    min_x: float
    min_y: float
    min_z: float
    max_x: float
    max_y: float
    max_z: float
    is_valid: bool

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            Double(self.min_x)
            | Double(self.min_y)
            | Double(self.min_z)
            | Double(self.max_x)
            | Double(self.max_y)
            | Double(self.max_z)
            | U8Bool(self.is_valid),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                Double("min_x")
                | Double("min_y")
                | Double("min_z")
                | Double("max_x")
                | Double("max_y")
                | Double("max_z")
                | U8Bool("is_valid"),
            ),
        )


@float_eq(float_slots=("value",))
class FluidBox(pydantic.BaseModel):
    value: float

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Float(self.value))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls(
            value=des.get_struct(Float, first=True),
        )


@pydantic_eq
class InventoryItem(pydantic.BaseModel):
    unknown: int

    name: str
    unknown_2: int | None = None
    type: str | None = None
    properties: "PropertyList | None" = None

    def __serialize__(self, ser: "Serializer") -> None:
        has_properties = self.type is not None and self.properties is not None
        ser.add_struct(U32(self.unknown) | String(self.name) | U32Bool(has_properties))
        if has_properties:
            ns = ser.new()
            ns.add(typing.cast("PropertyList", self.properties))  # type: ignore
            ser.add_struct(
                U32(typing.cast("int", self.unknown_2)) | String(self.type) | Raw.with_len(ns.content),
            )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        from sat_save_tools.models.properties import PropertyList  # noqa: PLC0415

        content = des.get_dict(U32("unknown") | String("name") | U32Bool("has_properties"))
        if content["has_properties"]:
            content |= des.get_dict(
                U32("unknown_2") | String("type") | U32("properties_size") | Object(PropertyList)("properties"),
            )
        return cls.model_validate(content)


@float_eq(float_slots=("r", "g", "b", "a"))
class LinearColor(pydantic.BaseModel):
    r: float
    g: float
    b: float
    a: float

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Float(self.r) | Float(self.g) | Float(self.b) | Float(self.a))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(des.get_dict(Float("r") | Float("g") | Float("b") | Float("a")))


@float_eq(double_slots=("x", "y", "z", "w"))
class DoubleQuaternion(pydantic.BaseModel):
    x: float
    y: float
    z: float
    w: float

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Double(self.x) | Double(self.y) | Double(self.z) | Double(self.w))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(des.get_dict(Double("x") | Double("y") | Double("z") | Double("w")))


@float_eq(float_slots=("x", "y", "z", "w"))
class FloatQuaternion(pydantic.BaseModel):
    x: float
    y: float
    z: float
    w: float

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Float(self.x) | Float(self.y) | Float(self.z) | Float(self.w))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(des.get_dict(Float("x") | Float("y") | Float("z") | Float("w")))


@float_eq(float_slots=("offset", "forward"), other_slots=("object_reference",))
class RailroadTrackPosition(pydantic.BaseModel):
    object_reference: ObjectReference
    offset: float
    forward: float

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Object(self.object_reference) | Float(self.offset) | Float(self.forward))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(Object(ObjectReference)("object_reference") | Float("offset") | Float("forward")),
        )


@float_eq(float_slots=("x", "y", "z"))
class FloatVector3(pydantic.BaseModel):
    x: float
    y: float
    z: float

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Float(self.x) | Float(self.y) | Float(self.z))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(des.get_dict(Float("x") | Float("y") | Float("z")))


@float_eq(double_slots=("x", "y", "z"))
class DoubleVector3(pydantic.BaseModel):
    x: float
    y: float
    z: float

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Double(self.x) | Double(self.y) | Double(self.z))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(des.get_dict(Double("x") | Double("y") | Double("z")))


@pydantic_eq
class DateTime(pydantic.BaseModel):
    value: int

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(I64(self.value))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls(value=des.get_struct(I64, first=True))


class ClientIdentityInfoIdentityVariant(U8EnumSerializerMixin, U8EnumDeserializerMixin, enum.IntEnum):
    EPIC = 1
    STEAM = 6


@pydantic_eq
class ClientIdentityInfoIdentity(pydantic.BaseModel):
    variant: ClientIdentityInfoIdentityVariant
    payload: pydantic.Base64Bytes

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Object(self.variant) | Raw.with_len(self.payload))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(Object(ClientIdentityInfoIdentityVariant)("variant") | U32("size"))
        content |= des.get_dict(B64Raw(content["size"])("payload"))
        return cls.model_validate(content)


@pydantic_eq
class ClientIdentityInfo(pydantic.BaseModel):
    uuid: str
    identities: list[ClientIdentityInfoIdentity]

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(String(self.uuid) | U32(len(self.identities)) | Struct.from_iter(Object, self.identities))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(String("uuid") | U32("identities_length"))
        content["identities"] = des.get_struct(Object(ClientIdentityInfoIdentity) * content["identities_length"])
        return cls.model_validate(content)


@pydantic_eq
class SpawnData(pydantic.BaseModel):
    name: str
    type: typing.Literal["ObjectProperty"]
    level_path: ObjectReference
    properties: "PropertyList"

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add(self.level_path)

        ser.add_struct(
            String(self.name)
            | String(self.type)
            | U32(len(ns))
            | U32(0)
            | U8(0)
            | Raw(len(ns))(ns.content)
            | Object(self.properties),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        from sat_save_tools.models.properties import PropertyList  # noqa: PLC0415

        return cls.model_validate(
            des.get_dict(
                String("name")
                | String("type")
                | U32("size")
                | U32("unknown")
                | U8("unknown_2")
                | Object(ObjectReference)("level_path")
                | Object(PropertyList)("properties"),
            ),
        )


@pydantic_eq
class GUID(pydantic.BaseModel):
    guid: pydantic.Base64Bytes | None = None

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U8Bool(self.guid is not None))
        if self.guid is not None:
            ser.add_raw(self.guid)

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        has_guid = des.get_struct(U8Bool, first=True)
        guid = b64_bytes(des.get_raw(16)) if has_guid else None
        return cls(guid=guid)


class UUIDGUID(uuid.UUID):
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: type[typing.Any],
        handler: collections.abc.Callable[..., typing.Any],
    ) -> typing.Any:
        from pydantic_core import core_schema  # noqa: PLC0415

        return core_schema.uuid_schema()

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_raw(self.bytes)

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        raw_bytes = bytes(des.get_raw(16))
        return cls(bytes=raw_bytes)


type StructValue = typing.Union[  # noqa: UP007
    LinearColor,
    SpawnData,
    DoubleQuaternion,
    Box,
    InventoryItem,
    FluidBox,
    RailroadTrackPosition,
    DateTime,
    ClientIdentityInfo,
    DoubleVector3,
    GUID,
    UUIDGUID,
    "PropertyList",
]


@set_struct_name("StructValue")
def deserialize_struct_value(  # noqa: PLR0911
    des: "Deserializer",
    struct_type: StructTypeName,
    payload_size: int,
) -> StructValue | pydantic.Base64Bytes:
    from sat_save_tools.models.properties import PropertyList  # noqa: PLC0415

    scruct_start_offset = des.offset
    try:
        match struct_type:
            case StructTypeName.LINEAR_COLOR | StructTypeName.COLOR:
                return des.get(LinearColor)
            case StructTypeName.VECTOR:
                return des.get(DoubleVector3)
            case StructTypeName.VECTOR | StructTypeName.ROTATOR:
                return des.get(DoubleVector3)
            case StructTypeName.QUAT:
                return des.get(DoubleQuaternion)
            case StructTypeName.BOX:
                return des.get(Box)
            case StructTypeName.INVENTORY_ITEM:
                return des.get(InventoryItem)
            case StructTypeName.FLUID_BOX:
                return des.get(FluidBox)
            case StructTypeName.RAILROAD_TRACK_POSITION:
                return des.get(RailroadTrackPosition)
            case StructTypeName.DATE_TIME:
                return des.get(DateTime)
            case StructTypeName.CLIENT_IDENTITY_INFO:
                return des.get(ClientIdentityInfo)
            case StructTypeName.GUID:
                try:
                    return des.get(GUID)
                except (SatisfactorySaveParserError, ValueError):
                    des.offset = scruct_start_offset
                    return des.get(UUIDGUID)
            case _:
                return des.get(PropertyList)
    except (SatisfactorySaveParserError, ValueError) as exc:
        des.offset = scruct_start_offset
        if logger.isEnabledFor(logging.WARNING):
            logger.warning("Failed to deserialize struct type %s, returning raw bytes", struct_type)
            logger.warning("Error %s", exc)
        return des.get_raw(payload_size)
