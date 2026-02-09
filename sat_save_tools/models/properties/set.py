import enum
import logging
import typing

import pydantic

from sat_save_tools.dev import dev_dump_unparsed_chunk
from sat_save_tools.models.properties.array import ObjectReference
from sat_save_tools.models.properties.base import BaseProperty
from sat_save_tools.models.properties.enums import PropertyTypeName
from sat_save_tools.serde import U8, U32, U64, Object, Raw, String
from sat_save_tools.utils import (
    StrEnumDeserializerMixin,
    StrEnumSerializerMixin,
    b64_bytes,
    expect_size,
)

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializable, Serializer


__all__ = (
    "SetProperty",
    "SetType",
)

logger = logging.getLogger()


class SetType(StrEnumSerializerMixin, StrEnumDeserializerMixin, enum.StrEnum):
    U_INT_32 = "UInt32Property"
    STRUCT = "StructProperty"
    OBJECT = "ObjectProperty"


class SetProperty(BaseProperty[list[ObjectReference] | list[int] | list[tuple[int, int]] | pydantic.Base64Bytes]):
    type_name: typing.Literal[PropertyTypeName.SET] = PropertyTypeName.SET
    set_type: SetType
    index: int
    unk1: int
    length: int

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_string(self.name)
        ser.add(self.type_name)

        ns = ser.new()
        ns.add_struct(U32(self.unk1))
        if isinstance(self.value, bytes):
            ns.add_struct(U32(self.length) | Raw(len(self.value))(self.value))
        else:
            ns.add_struct(U32(len(self.value)))
            for it in self.value:
                match self.set_type:
                    case SetType.OBJECT:
                        ns.add(typing.cast("Serializable", it))
                    case SetType.U_INT_32:
                        ns.add_struct(U32(typing.cast("int", it)))
                    case SetType.STRUCT:
                        itt = typing.cast("tuple[int, int]", it)
                        ns.add_struct(U64(itt[0]) | U64(itt[1]))

        ser.add_struct(
            U32(len(ns)) | U32(self.index) | Object(self.set_type) | U8(0) | Raw(len(ns.content))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            String("name")
            | Object(PropertyTypeName)("type_name")
            | U32("payload_size")
            | U32("index")
            | Object(SetType)("set_type")
            | U8("padding"),
        )
        with expect_size(des, content["payload_size"], "SetProperty"):
            content |= des.get_dict(U32("unk1") | U32("length"))

            value_bytes = des.get_raw(content["payload_size"] - 8)
            value_des = des.new(value_bytes)

            values = []
            for _ in range(content["length"]):
                match content["set_type"]:
                    case SetType.OBJECT:
                        values.append(value_des.get(ObjectReference))
                    case SetType.U_INT_32:
                        values.append(value_des.get_struct(U32)[0])
                    case SetType.STRUCT:
                        values.append(value_des.get_struct(U64 | U64))
                    case _:
                        dev_dump_unparsed_chunk(
                            "set_property",
                            str(content["set_type"]),
                            content=value_bytes,
                        )
                        if logger.isEnabledFor(logging.WARNING):
                            logger.warning(
                                "Deserializer for set element with type %r not found",
                                content["set_type"],
                            )
                        break
            content["value"] = values or b64_bytes(value_bytes)
            return cls.model_validate(content)
