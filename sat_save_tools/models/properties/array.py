import logging
import math
import typing

import pydantic

from sat_save_tools.models.object_reference import ObjectReference
from sat_save_tools.models.properties.base import BaseProperty
from sat_save_tools.models.properties.enums import (
    ArrayElementTypeName,
    PropertyTypeName,
    StructTypeName,
)
from sat_save_tools.models.properties.typed_data import (
    StructValue,
    deserialize_struct_value,
)
from sat_save_tools.serde import (
    I32,
    I64,
    U8,
    U32,
    B64Raw,
    Float,
    Object,
    Raw,
    String,
    Struct,
)
from sat_save_tools.utils import b64_bytes, expect_size, pydantic_eq

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializer


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
    "ArrayProperty",
    "BaseArrayElement",
)


logger = logging.getLogger()


@pydantic_eq
class BaseArrayElement[T](pydantic.BaseModel):
    length: int
    elements: T

    def __serialize__(self, ser: "Serializer") -> None:
        raise NotImplementedError

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        raise NotImplementedError


class ArrayElementByte(BaseArrayElement[pydantic.Base64Bytes]):
    type: typing.Literal[ArrayElementTypeName.BYTE] = ArrayElementTypeName.BYTE
    elements: pydantic.Base64Bytes

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(Raw.with_len(self.elements))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        length = des.get_struct(U32, first=True)
        elements = des.get_raw(length)
        return cls(
            length=length,
            elements=b64_bytes(elements),
        )


class ArrayElementEnum(BaseArrayElement[list[str]]):
    type: typing.Literal[ArrayElementTypeName.ENUM] = ArrayElementTypeName.ENUM

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(len(self.elements)) | Struct.from_iter(String, self.elements),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("length"))
        content["elements"] = des.get_struct(String() * content["length"])
        return cls.model_validate(content)


class ArrayElementStr(BaseArrayElement[list[str]]):
    type: typing.Literal[ArrayElementTypeName.STR] = ArrayElementTypeName.STR

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(len(self.elements)) | Struct.from_iter(String, self.elements),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("length"))
        content["elements"] = des.get_struct(String() * content["length"])
        return cls.model_validate(content)


class ArrayElementInterface(BaseArrayElement[list[ObjectReference]]):
    type: typing.Literal[ArrayElementTypeName.INTERFACE] = ArrayElementTypeName.INTERFACE

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(len(self.elements)) | Struct.from_iter(Object, self.elements),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("length"))
        content["elements"] = des.get_struct(
            Object(ObjectReference) * content["length"],
        )
        return cls.model_validate(content)


class ArrayElementObject(BaseArrayElement[list[ObjectReference]]):
    type: typing.Literal[ArrayElementTypeName.OBJECT] = ArrayElementTypeName.OBJECT

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            U32(len(self.elements)) | Struct.from_iter(Object, self.elements),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("length"))
        content["elements"] = des.get_struct(
            Object(ObjectReference) * content["length"],
        )
        return cls.model_validate(content)


class ArrayElementInt(BaseArrayElement[list[int]]):
    type: typing.Literal[ArrayElementTypeName.INT] = ArrayElementTypeName.INT

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(len(self.elements)) | Struct.from_iter(I32, self.elements))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("length"))
        content["elements"] = des.get_struct(I32 * content["length"])
        return cls.model_validate(content)


class ArrayElementInt64(BaseArrayElement[list[int]]):
    type: typing.Literal[ArrayElementTypeName.INT64] = ArrayElementTypeName.INT64

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(len(self.elements)) | Struct.from_iter(I64, self.elements))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("length"))
        content["elements"] = des.get_struct(I64 * content["length"])
        return cls.model_validate(content)


class ArrayElementFloat(BaseArrayElement[list[float]]):
    type: typing.Literal[ArrayElementTypeName.FLOAT] = ArrayElementTypeName.FLOAT

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ArrayElementFloat):
            return NotImplemented
        return all(
            [
                self.type == value.type,
                self.length == value.length,
                all(
                    math.isclose(self_el, other_el, rel_tol=1e-6, abs_tol=1e-12)
                    for self_el, other_el in zip(
                        self.elements,
                        value.elements,
                        strict=True,
                    )
                ),
            ],
        )

    __hash__ = None

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(len(self.elements)) | Struct.from_iter(Float, self.elements))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("length"))
        content["elements"] = des.get_struct(Float * content["length"])
        return cls.model_validate(content)


class ArrayElementSoftObject(BaseArrayElement[list[tuple[ObjectReference, int]]]):
    type: typing.Literal[ArrayElementTypeName.SOFT_OBJECT] = ArrayElementTypeName.SOFT_OBJECT

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(len(self.elements)))
        for it in self.elements:
            ser.add(it[0])
            ser.add_struct(U32(it[1]))

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(U32("length"))
        content["elements"] = [des.get_struct(Object(ObjectReference) | U32) for _ in range(content["length"])]
        return cls.model_validate(content)


type ArrayElementStructValueType = list[StructValue] | pydantic.Base64Bytes


class ArrayElementStruct(BaseArrayElement[ArrayElementStructValueType]):
    type: typing.Literal[ArrayElementTypeName.STRUCT] = ArrayElementTypeName.STRUCT
    name: str
    type_name: str
    payload_size: int
    element_type: StructTypeName
    uuid: pydantic.Base64Bytes

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(self.length) | String(self.name) | String(self.type_name))

        ns = ser.new()
        if isinstance(self.elements, list):
            for it in self.elements:
                ns.add(it)
        else:
            ns.add_raw(self.elements)

        ser.add_struct(
            U32(len(ns))
            | U32(0)
            | Object(self.element_type)
            | Raw(len(self.uuid))(self.uuid)
            | Raw(len(ns.content))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            U32("length")
            | String("name")
            | String("type_name")
            | U32("payload_size")
            | U32("unknown")
            | Object(StructTypeName)("element_type")
            | B64Raw(17)("uuid"),
        )

        with expect_size(des, content["payload_size"], "ArrayElementStruct"):
            elements = []
            start_property_offset = des.offset
            for _ in range(content["length"]):
                element = des.get_fn(
                    deserialize_struct_value,
                    struct_type=content["element_type"],
                    payload_size=content["payload_size"],
                )
                if isinstance(element, (bytes, bytearray, memoryview)):
                    des.offset = start_property_offset
                    elements = b64_bytes(des.get_raw(content["payload_size"]))
                    break
                elements.append(element)
            content["elements"] = elements
        return cls.model_validate(content)


type ArrayElementType = typing.Annotated[
    ArrayElementByte
    | ArrayElementEnum
    | ArrayElementStr
    | ArrayElementInterface
    | ArrayElementObject
    | ArrayElementInt
    | ArrayElementInt64
    | ArrayElementFloat
    | ArrayElementSoftObject
    | ArrayElementStruct,
    pydantic.Field(discriminator="type"),
]


class ArrayProperty(BaseProperty[ArrayElementType]):
    type_name: typing.Literal[PropertyTypeName.ARRAY] = PropertyTypeName.ARRAY
    index: int

    def __serialize__(self, ser: "Serializer") -> None:
        ns = ser.new()
        ns.add(self.value)
        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.value.type)
            | U8(0),
        )
        ser.add(ns)

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            String("name")
            | Object(PropertyTypeName)("type_name")
            | U32("payload_size")
            | U32("index")
            | Object(ArrayElementTypeName)("element_type")
            | U8("padding"),
        )

        with expect_size(des, content["payload_size"], "ArrayProperty"):
            match content["element_type"]:
                case ArrayElementTypeName.BYTE:
                    content["value"] = des.get(ArrayElementByte)
                case ArrayElementTypeName.ENUM:
                    content["value"] = des.get(ArrayElementEnum)
                case ArrayElementTypeName.STR:
                    content["value"] = des.get(ArrayElementStr)
                case ArrayElementTypeName.INTERFACE:
                    content["value"] = des.get(ArrayElementInterface)
                case ArrayElementTypeName.OBJECT:
                    content["value"] = des.get(ArrayElementObject)
                case ArrayElementTypeName.INT:
                    content["value"] = des.get(ArrayElementInt)
                case ArrayElementTypeName.INT64:
                    content["value"] = des.get(ArrayElementInt64)
                case ArrayElementTypeName.FLOAT:
                    content["value"] = des.get(ArrayElementFloat)
                case ArrayElementTypeName.SOFT_OBJECT:
                    content["value"] = des.get(ArrayElementSoftObject)
                case ArrayElementTypeName.STRUCT:
                    content["value"] = des.get(ArrayElementStruct)
                case _:
                    typing.assert_never(content["element_type"])
        return cls.model_validate(content)
