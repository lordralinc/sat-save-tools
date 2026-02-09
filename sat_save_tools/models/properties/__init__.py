import typing

import pydantic

from sat_save_tools.utils import pydantic_eq

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Serializer

from .array import (
    ArrayElementByte,
    ArrayElementEnum,
    ArrayElementFloat,
    ArrayElementInt,
    ArrayElementInt64,
    ArrayElementInterface,
    ArrayElementObject,
    ArrayElementSoftObject,
    ArrayElementStr,
    ArrayElementStruct,
    ArrayElementStructValueType,
    ArrayElementType,
    ArrayProperty,
    BaseArrayElement,
)
from .base import BaseProperty
from .enums import ArrayElementTypeName, PropertyTypeName, StructTypeName
from .map import KeyTypeName, MapKeyType, MapKeyValue, MapProperty, ValueTypeName
from .set import SetProperty, SetType
from .simple_preperties import (
    BoolProperty,
    ByteProperty,
    DoubleProperty,
    EnumProperty,
    FloatProperty,
    Int8Property,
    Int64Property,
    IntProperty,
    NameProperty,
    ObjectProperty,
    SoftObjectProperty,
    StrProperty,
    UInt32Property,
)
from .struct import StructProperty
from .text import (
    TextArgument,
    TextArgumentInt,
    TextArgumentText,
    TextArgumentType,
    TextProperty,
    TextPropertyHistoryType,
    TextValue,
    TextValueBase,
    TextValueNone,
    TextValueStringTableEntry,
    TextValueTransform,
    TextValueWithArguments,
    deserialize_text_argument,
)
from .typed_data import (
    Box,
    ClientIdentityInfo,
    ClientIdentityInfoIdentity,
    ClientIdentityInfoIdentityVariant,
    DateTime,
    DoubleQuaternion,
    DoubleVector3,
    FloatQuaternion,
    FloatVector3,
    FluidBox,
    InventoryItem,
    LinearColor,
    RailroadTrackPosition,
    SpawnData,
)

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer


__all__ = (
    "ArrayElementByte",
    "ArrayElementEnum",
    "ArrayElementFloat",
    "ArrayElementInt",
    "ArrayElementInt64",
    "ArrayElementInterface",
    "ArrayElementObject",
    "ArrayElementSoftObject",
    "ArrayElementStr",
    "ArrayElementStruct",
    "ArrayElementStructValueType",
    "ArrayElementType",
    "ArrayElementTypeName",
    "ArrayProperty",
    "BaseArrayElement",
    "BaseProperty",
    "BoolProperty",
    "Box",
    "ByteProperty",
    "ClientIdentityInfo",
    "ClientIdentityInfoIdentity",
    "ClientIdentityInfoIdentityVariant",
    "DateTime",
    "DoubleProperty",
    "DoubleQuaternion",
    "DoubleVector3",
    "EnumProperty",
    "FloatProperty",
    "FloatQuaternion",
    "FloatVector3",
    "FluidBox",
    "Int8Property",
    "Int64Property",
    "IntProperty",
    "InventoryItem",
    "KeyTypeName",
    "LinearColor",
    "MapKeyType",
    "MapKeyValue",
    "MapProperty",
    "NameProperty",
    "ObjectProperty",
    "PropertyList",
    "PropertyType",
    "PropertyTypeName",
    "RailroadTrackPosition",
    "SetProperty",
    "SetType",
    "SoftObjectProperty",
    "SpawnData",
    "StrProperty",
    "StructProperty",
    "StructTypeName",
    "TextArgument",
    "TextArgumentInt",
    "TextArgumentText",
    "TextArgumentType",
    "TextProperty",
    "TextPropertyHistoryType",
    "TextValue",
    "TextValueBase",
    "TextValueNone",
    "TextValueStringTableEntry",
    "TextValueTransform",
    "TextValueWithArguments",
    "UInt32Property",
    "ValueTypeName",
    "deserialize_text_argument",
)

type PropertyType = typing.Annotated[
    ArrayProperty
    | BoolProperty
    | ByteProperty
    | DoubleProperty
    | EnumProperty
    | FloatProperty
    | Int8Property
    | Int64Property
    | IntProperty
    | NameProperty
    | ObjectProperty
    | SoftObjectProperty
    | StrProperty
    | UInt32Property
    | TextProperty
    | SetProperty
    | StructProperty
    | MapProperty,
    pydantic.Field(discriminator="type_name"),
]


@pydantic_eq
class PropertyList(pydantic.BaseModel):
    items: dict[str, PropertyType]

    @typing.overload
    def get_value_or_none(self, name: str, *, result: None = ...) -> PropertyType | None: ...
    @typing.overload
    def get_value_or_none[T](self, name: str, *, result: type[T] = ...) -> T | None: ...
    def get_value_or_none[T](self, name: str, *, result: type[T] | None = None) -> PropertyType | T | None:  # noqa: ARG002
        return self.items.get(name, None)

    @typing.overload
    def get_value(self, name: str, *, result: None = ...) -> PropertyType: ...
    @typing.overload
    def get_value[T](self, name: str, *, result: type[T] = ...) -> T: ...  # type: ignore
    def get_value[T](self, name: str, *, result: type[T] | None = None) -> PropertyType | T:
        if item := self.get_value_or_none(name, result=result):
            return item
        raise KeyError(f"Property with name '{name}' not found")

    def __serialize__(self, ser: "Serializer") -> None:
        for el in self.items.values():
            ser.add(el)
        ser.add_string("None")

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        properties = []
        while True:
            start_offset = des.offset
            name = des.get_string()
            if name == "None":
                break
            property_type = des.get(PropertyTypeName)
            des.offset = start_offset
            match property_type:
                case PropertyTypeName.ARRAY:
                    properties.append(des.get(ArrayProperty))
                case PropertyTypeName.BOOL:
                    properties.append(des.get(BoolProperty))
                case PropertyTypeName.BYTE:
                    properties.append(des.get(ByteProperty))
                case PropertyTypeName.ENUM:
                    properties.append(des.get(EnumProperty))
                case PropertyTypeName.FLOAT:
                    properties.append(des.get(FloatProperty))
                case PropertyTypeName.DOUBLE:
                    properties.append(des.get(DoubleProperty))
                case PropertyTypeName.INT:
                    properties.append(des.get(IntProperty))
                case PropertyTypeName.INT8:
                    properties.append(des.get(Int8Property))
                case PropertyTypeName.U_INT32:
                    properties.append(des.get(UInt32Property))
                case PropertyTypeName.INT64:
                    properties.append(des.get(Int64Property))
                case PropertyTypeName.NAME:
                    properties.append(des.get(NameProperty))
                case PropertyTypeName.OBJECT:
                    properties.append(des.get(ObjectProperty))
                case PropertyTypeName.SOFT_OBJECT:
                    properties.append(des.get(SoftObjectProperty))
                case PropertyTypeName.STR:
                    properties.append(des.get(StrProperty))
                case PropertyTypeName.TEXT:
                    properties.append(des.get(TextProperty))
                case PropertyTypeName.SET:
                    properties.append(des.get(SetProperty))
                case PropertyTypeName.STRUCT:
                    properties.append(des.get(StructProperty))
                case PropertyTypeName.MAP:
                    properties.append(des.get(MapProperty))
                case _:
                    typing.assert_never(property_type)
        return cls(items={it.name: it for it in properties})
