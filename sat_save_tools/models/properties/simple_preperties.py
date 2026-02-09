import typing

import pydantic

from sat_save_tools.models.object_reference import ObjectReference
from sat_save_tools.models.properties.base import BaseProperty
from sat_save_tools.models.properties.enums import PropertyTypeName
from sat_save_tools.models.properties.typed_data import GUID
from sat_save_tools.serde import (
    I8,
    I32,
    I64,
    U32,
    Double,
    Float,
    Object,
    Raw,
    String,
    U8Bool,
)
from sat_save_tools.utils import b64_bytes, float_eq

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializer


__all__ = (
    "BoolProperty",
    "ByteProperty",
    "DoubleProperty",
    "EnumProperty",
    "FloatProperty",
    "Int8Property",
    "Int64Property",
    "IntProperty",
    "NameProperty",
    "ObjectProperty",
    "SoftObjectProperty",
    "StrProperty",
    "UInt32Property",
)


class BoolProperty(BaseProperty[bool]):
    type_name: typing.Literal[PropertyTypeName.BOOL] = PropertyTypeName.BOOL
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(0)
            | U32(self.index)
            | U8Bool(self.value)
            | Object(self.guid),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("padding")
                | U32("index")
                | U8Bool("value")
                | Object(GUID)("guid"),
            ),
        )


class ByteProperty(BaseProperty[pydantic.Base64Bytes]):
    type_name: typing.Literal[PropertyTypeName.BYTE] = PropertyTypeName.BYTE
    index: int = 0
    type: str
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_raw(self.value)

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | String(self.type)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            String("name")
            | Object(PropertyTypeName)("type_name")
            | U32("payload_size")
            | U32("index")
            | String("type")
            | Object(GUID)("guid"),
        )
        content["value"] = b64_bytes(des.get_raw(content["payload_size"]))
        return cls.model_validate(content)


class EnumProperty(BaseProperty[str]):
    type_name: typing.Literal[PropertyTypeName.ENUM] = PropertyTypeName.ENUM
    index: int = 0
    type: str
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_string(self.value)

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | String(self.type)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | String("type")
                | Object(GUID)("guid")
                | String("value"),
            ),
        )


@float_eq(float_slots=("value",), other_slots=("name", "type_name", "index"))
class FloatProperty(BaseProperty[float]):
    type_name: typing.Literal[PropertyTypeName.FLOAT] = PropertyTypeName.FLOAT
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(Float(self.value))

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | Float("value"),
            ),
        )


@float_eq(double_slots=("value",), other_slots=("name", "type_name", "index"))
class DoubleProperty(BaseProperty[float]):
    type_name: typing.Literal[PropertyTypeName.DOUBLE] = PropertyTypeName.DOUBLE
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(Double(self.value))

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | Double("value"),
            ),
        )


class IntProperty(BaseProperty[int]):
    type_name: typing.Literal[PropertyTypeName.INT] = PropertyTypeName.INT
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(I32(self.value))

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | I32("value"),
            ),
        )


class Int8Property(BaseProperty[int]):
    type_name: typing.Literal[PropertyTypeName.INT8] = PropertyTypeName.INT8
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(I8(self.value))

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | I8("value"),
            ),
        )


class UInt32Property(BaseProperty[int]):
    type_name: typing.Literal[PropertyTypeName.U_INT32] = PropertyTypeName.U_INT32
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(U32(self.value))

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | U32("value"),
            ),
        )


class Int64Property(BaseProperty[int]):
    type_name: typing.Literal[PropertyTypeName.INT64] = PropertyTypeName.INT64
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(I64(self.value))

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | I64("value"),
            ),
        )


class NameProperty(BaseProperty[str]):
    type_name: typing.Literal[PropertyTypeName.NAME] = PropertyTypeName.NAME
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_string(self.value)

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | String("value"),
            ),
        )


class StrProperty(BaseProperty[str]):
    type_name: typing.Literal[PropertyTypeName.STR] = PropertyTypeName.STR
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_string(self.value)

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | String("value"),
            ),
        )


class ObjectProperty(BaseProperty[ObjectReference]):
    type_name: typing.Literal[PropertyTypeName.OBJECT] = PropertyTypeName.OBJECT
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(Object(self.value))

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(PropertyTypeName)("type_name")
                | U32("payload_size")
                | U32("index")
                | Object(GUID)("guid")
                | Object(ObjectReference)("value"),
            ),
        )


class SoftObjectProperty(BaseProperty[tuple[ObjectReference, int]]):
    type_name: typing.Literal[PropertyTypeName.SOFT_OBJECT] = PropertyTypeName.SOFT_OBJECT
    index: int = 0
    guid: GUID = GUID()

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add_struct(Object(self.value[0]) | U32(self.value[1]))

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.guid)
            | Raw(len(ns))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            String("name")
            | Object(PropertyTypeName)("type_name")
            | U32("payload_size")
            | U32("index")
            | Object(GUID)("guid"),
        )
        content["value"] = des.get_struct(Object(ObjectReference) | U32)

        return cls.model_validate(content)
