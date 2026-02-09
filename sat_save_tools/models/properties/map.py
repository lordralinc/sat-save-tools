import enum
import math
import typing

from sat_save_tools.models.properties.array import ObjectReference
from sat_save_tools.models.properties.base import BaseProperty
from sat_save_tools.models.properties.enums import (
    PropertyTypeName,
    StrEnumSerializerMixin,
)
from sat_save_tools.models.properties.text import TextProperty, TextValue
from sat_save_tools.serde import (
    I32,
    I64,
    U8,
    U32,
    Double,
    Float,
    Object,
    Raw,
    Serializable,
    Serializer,
    String,
    U8Bool,
)
from sat_save_tools.utils import StrEnumDeserializerMixin, expect_size

if typing.TYPE_CHECKING:
    from sat_save_tools.models.properties import PropertyList
    from sat_save_tools.serde import Deserializer

__all__ = (
    "KeyTypeName",
    "MapKeyType",
    "MapKeyValue",
    "MapProperty",
    "ValueTypeName",
)


class KeyTypeName(StrEnumSerializerMixin, StrEnumDeserializerMixin, enum.StrEnum):
    OBJECT = "ObjectProperty"
    INT = "IntProperty"
    INT64 = "Int64Property"
    NAME = "NameProperty"
    STR = "StrProperty"
    ENUM = "EnumProperty"
    STRUCT = "StructProperty"


class ValueTypeName(StrEnumSerializerMixin, StrEnumDeserializerMixin, enum.StrEnum):
    BYTE = "ByteProperty"
    BOOL = "BoolProperty"
    INT = "IntProperty"
    INT64 = "Int64Property"
    FLOAT = "FloatProperty"
    DOUBLE = "DoubleProperty"
    STR = "StrProperty"
    OBJECT = "ObjectProperty"
    TEXT = "TextProperty"
    STRUCT = "StructProperty"


type MapKeyType = ObjectReference | int | str | tuple[int, int, int]
type MapKeyValue = "int | str | ObjectReference | TextProperty | float | PropertyList | TextValue"


class MapProperty(BaseProperty[list[tuple[MapKeyType, MapKeyValue]]]):
    type_name: typing.Literal[PropertyTypeName.MAP] = PropertyTypeName.MAP
    index: int
    key_type: KeyTypeName
    value_type: ValueTypeName
    mode: int

    __hash__ = None

    def __eq__(self, other: object) -> bool:  # noqa: PLR0911
        if not isinstance(other, MapProperty):
            return NotImplemented

        if (
            self.type_name != other.type_name
            or self.index != other.index
            or self.key_type != other.key_type
            or self.value_type != other.value_type
            or self.mode != other.mode
        ):
            return False

        if len(self.value) != len(other.value):
            return False

        if self.value_type not in (ValueTypeName.FLOAT, ValueTypeName.DOUBLE):
            return self.value == other.value

        rel_tol = 1e-6 if self.value_type is ValueTypeName.FLOAT else 1e-9

        for item_idx in range(len(self.value)):
            a = self.value[item_idx][1]
            b = other.value[item_idx][1]

            if a is None or b is None:
                if a is b:
                    continue
                return False

            if not math.isclose(a, b, rel_tol=rel_tol, abs_tol=1e-12):  # type: ignore
                return False

        return True

    def __serialize__(self, ser: Serializer) -> None:
        ns = ser.new()
        ns.add_struct(U32(self.mode) | U32(len(self.value)))

        for key, value in self.value:
            match self.key_type:
                case KeyTypeName.INT:
                    ns.add_struct(I32(typing.cast("int", key)))
                case KeyTypeName.INT64:
                    ns.add_struct(I64(typing.cast("int", key)))
                case KeyTypeName.NAME | KeyTypeName.STR | KeyTypeName.ENUM:
                    ns.add_string(typing.cast("str", key))
                case KeyTypeName.OBJECT:
                    k = typing.cast("ObjectReference", key)
                    ns.add(k)
                case KeyTypeName.STRUCT:
                    k = typing.cast("tuple[int, int, int]", key)
                    ns.add_struct(I32(k[0]) | I32(k[1]) | I32(k[2]))
                case _:
                    typing.assert_never(self.key_type)
            match self.value_type:
                case ValueTypeName.BYTE:
                    if self.key_type == KeyTypeName.STR:
                        ns.add_string(typing.cast("str", value))
                    else:
                        ns.add_struct(U8(typing.cast("int", value)))
                case ValueTypeName.BOOL:
                    ns.add_struct(U8Bool(typing.cast("bool", value)))
                case ValueTypeName.INT:
                    ns.add_struct(I32(typing.cast("int", value)))
                case ValueTypeName.INT64:
                    ns.add_struct(I64(typing.cast("int", value)))
                case ValueTypeName.FLOAT:
                    ns.add_struct(Float(typing.cast("float", value)))
                case ValueTypeName.DOUBLE:
                    ns.add_struct(Double(typing.cast("float", value)))
                case ValueTypeName.STR:
                    ns.add_string(typing.cast("str", value))
                case ValueTypeName.OBJECT | ValueTypeName.TEXT:
                    ns.add(typing.cast("Serializable", value))
                case ValueTypeName.STRUCT:
                    ns.add(typing.cast("PropertyList", value))
                case _:
                    typing.assert_never(self.value_type)

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.key_type)
            | Object(self.value_type)
            | U8(0)
            | Raw(len(ns.content))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        from sat_save_tools.models.properties import PropertyList  # noqa: PLC0415

        content = des.get_dict(
            String("name")
            | Object(PropertyTypeName)("type_name")
            | U32("payload_size")
            | U32("index")
            | Object(KeyTypeName)("key_type")
            | Object(ValueTypeName)("value_type")
            | U8("padding"),
        )
        with expect_size(des, content["payload_size"], "MapProperty"):
            content |= des.get_dict(U32("mode") | U32("elements_count"))
            elemets = []

            for _ in range(content["elements_count"]):
                match typing.cast("KeyTypeName", content["key_type"]):
                    case KeyTypeName.INT:
                        key = des.get_struct(I32, first=True)
                    case KeyTypeName.INT64:
                        key = des.get_struct(I64, first=True)
                    case KeyTypeName.NAME | KeyTypeName.STR | KeyTypeName.ENUM:
                        key = des.get_string()
                    case KeyTypeName.OBJECT:
                        key = des.get(ObjectReference)
                    case KeyTypeName.STRUCT:
                        key = des.get_struct(I32 * 3)
                    case _ as kt:
                        typing.assert_never(kt)
                match typing.cast("ValueTypeName", content["value_type"]):
                    case ValueTypeName.BYTE:
                        value = (
                            des.get_string()
                            if typing.cast("KeyTypeName", content["key_type"]) == KeyTypeName.STR
                            else des.get_struct(U8)[0]
                        )
                    case ValueTypeName.BOOL:
                        value = des.get_struct(U8Bool)[0]
                    case ValueTypeName.INT:
                        value = des.get_struct(I32)[0]
                    case ValueTypeName.INT64:
                        value = des.get_struct(I64)[0]
                    case ValueTypeName.FLOAT:
                        value = des.get_struct(Float)[0]
                    case ValueTypeName.DOUBLE:
                        value = des.get_struct(Double)[0]
                    case ValueTypeName.STR:
                        value = des.get_string()
                    case ValueTypeName.OBJECT:
                        value = des.get(ObjectReference)
                    case ValueTypeName.TEXT:
                        value = des.get_fn(TextProperty.deserialize_property_value)
                    case ValueTypeName.STRUCT:
                        value = des.get(PropertyList)
                    case _ as vt:
                        typing.assert_never(vt)
                elemets.append((key, value))
            content["value"] = elemets
        return cls.model_validate(content)
