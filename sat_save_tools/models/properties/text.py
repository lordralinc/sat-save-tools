import enum
import typing

import pydantic

from sat_save_tools.logger import set_struct_name
from sat_save_tools.models.properties.base import BaseProperty
from sat_save_tools.models.properties.enums import PropertyTypeName
from sat_save_tools.serde import (
    I32,
    U8,
    U32,
    Function,
    Object,
    Raw,
    String,
    Struct,
    U32Bool,
)
from sat_save_tools.utils import (
    U8EnumDeserializerMixin,
    U8EnumSerializerMixin,
    pydantic_eq,
)

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializer

__all__ = (
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
    "deserialize_text_argument",
)


class TextPropertyHistoryType(U8EnumSerializerMixin, U8EnumDeserializerMixin, enum.IntEnum):
    BASE = 0
    NAMED = 1
    ARGUMENT = 3
    TRANSFORM = 10
    STRING_TABLE_ENTRY = 11
    NONE = 255


@pydantic_eq
class TextValueBase(pydantic.BaseModel):
    history_type: typing.Literal[TextPropertyHistoryType.BASE] = TextPropertyHistoryType.BASE
    flags: int
    namespace: str
    key: str
    value: str

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(self.flags)
            | Object(self.history_type)
            | String(self.namespace)
            | String(self.key)
            | String(self.value),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                U32("flags")
                | Object(TextPropertyHistoryType)("history_type")
                | String("namespace")
                | String("key")
                | String("value"),
            ),
        )


class TextArgumentType(U8EnumSerializerMixin, U8EnumDeserializerMixin, enum.IntEnum):
    INT = 0
    UINT = 1
    GENDER = 5
    FLOAT = 2
    DOUBLE = 3
    TEXT = 4


@pydantic_eq
class TextArgumentInt(pydantic.BaseModel):
    name: str
    value_type: typing.Literal[TextArgumentType.INT] = TextArgumentType.INT
    value: int
    unknown: int

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            String(self.name) | Object(self.value_type) | I32(self.value) | I32(self.unknown),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name") | Object(TextArgumentType)("value_type") | I32("value") | I32("unknown"),
            ),
        )


@pydantic_eq
class TextArgumentText(pydantic.BaseModel):
    name: str
    value_type: typing.Literal[TextArgumentType.TEXT] = TextArgumentType.TEXT
    value: "TextValue"

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(String(self.name) | Object(self.value_type) | Object(self.value))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("name")
                | Object(TextArgumentType)("value_type")
                | Function(TextProperty.deserialize_property_value)("value"),
            ),
        )


type TextArgument = typing.Annotated[
    TextArgumentInt | TextArgumentText,
    pydantic.Field(discriminator="value_type"),
]


@set_struct_name("TextArgument")
def deserialize_text_argument(des: "Deserializer") -> TextArgument:
    nd = des.copy()
    value_type: TextArgumentType = nd.get_struct(String() | Object(TextArgumentType))[1]
    match value_type:
        case TextArgumentType.INT:
            return des.get(TextArgumentInt)
        case TextArgumentType.TEXT:
            return des.get(TextArgumentText)
        case _:
            raise NotImplementedError(f"Deserializer for {value_type!r} not implemented")


@pydantic_eq
class TextValueWithArguments(pydantic.BaseModel):
    history_type: typing.Literal[TextPropertyHistoryType.NAMED, TextPropertyHistoryType.ARGUMENT] = (
        TextPropertyHistoryType.NAMED
    )

    source_format: "TextValue"
    flags: int
    arguments: list[TextArgument]

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(self.flags)
            | Object(self.history_type)
            | Object(self.source_format)
            | U32(len(self.arguments))
            | Struct.from_iter(Object, self.arguments),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            U32("flags")
            | Object(TextPropertyHistoryType)("history_type")
            | Function(TextProperty.deserialize_property_value)("source_format")
            | U32("argument_count"),
        )
        content["arguments"] = des.get_struct(Function(deserialize_text_argument) * content["argument_count"])
        return cls.model_validate(content)


@pydantic_eq
class TextValueTransform(pydantic.BaseModel):
    history_type: typing.Literal[TextPropertyHistoryType.TRANSFORM] = TextPropertyHistoryType.TRANSFORM
    source_text: "TextValue"
    transform_type: int
    flags: int

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(self.flags) | Object(self.history_type) | Object(self.source_text) | U8(self.transform_type),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                U32("flags")
                | Object(TextPropertyHistoryType)("history_type")
                | Function(TextProperty.deserialize_property_value)("source_text")
                | U8("transform_type"),
            ),
        )


@pydantic_eq
class TextValueStringTableEntry(pydantic.BaseModel):
    history_type: typing.Literal[TextPropertyHistoryType.STRING_TABLE_ENTRY] = (
        TextPropertyHistoryType.STRING_TABLE_ENTRY
    )
    table_id: str
    table_key: str
    flags: int

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(self.flags) | Object(self.history_type) | String(self.table_id) | String(self.table_key),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                U32("flags")
                | Object(TextPropertyHistoryType)("history_type")
                | String("table_id")
                | String("table_key"),
            ),
        )


@pydantic_eq
class TextValueNone(pydantic.BaseModel):
    history_type: typing.Literal[TextPropertyHistoryType.NONE] = TextPropertyHistoryType.NONE
    has_culture_invariant_string: bool
    value: str
    flags: int

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(self.flags)
            | Object(self.history_type)
            | U32Bool(self.has_culture_invariant_string)
            | String(self.value),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                U32("flags")
                | Object(TextPropertyHistoryType)("history_type")
                | U32Bool("has_culture_invariant_string")
                | String("value"),
            ),
        )


type TextValue = typing.Annotated[
    TextValueBase | TextValueWithArguments | TextValueTransform | TextValueStringTableEntry | TextValueNone,
    pydantic.Field(discriminator="history_type"),
]


class TextProperty(BaseProperty[TextValue]):
    type_name: typing.Literal[PropertyTypeName.TEXT] = PropertyTypeName.TEXT
    index: int

    @classmethod
    @set_struct_name("TextValue")
    def deserialize_property_value(cls, des: "Deserializer") -> TextValue:
        nd = des.copy()
        history_type: TextPropertyHistoryType = nd.get_struct(U32 | Object(TextPropertyHistoryType))[1]
        match history_type:
            case TextPropertyHistoryType.BASE:
                return des.get(TextValueBase)
            case TextPropertyHistoryType.NAMED:
                return des.get(TextValueWithArguments)
            case TextPropertyHistoryType.ARGUMENT:
                return des.get(TextValueWithArguments)
            case TextPropertyHistoryType.TRANSFORM:
                return des.get(TextValueTransform)
            case TextPropertyHistoryType.STRING_TABLE_ENTRY:
                return des.get(TextValueStringTableEntry)
            case TextPropertyHistoryType.NONE:
                return des.get(TextValueNone)
            case _:
                typing.assert_never(history_type)

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add(self.value)

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | U8(0)
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
                | U8("padding")
                | Function(cls.deserialize_property_value)("value"),
            ),
        )
