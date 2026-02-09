import logging
import typing

import pydantic

from sat_save_tools.models.properties.base import BaseProperty
from sat_save_tools.models.properties.enums import PropertyTypeName, StructTypeName
from sat_save_tools.models.properties.typed_data import (
    StructValue,
    deserialize_struct_value,
)
from sat_save_tools.serde import U32, B64Raw, Function, Object, Raw, Serializer, String
from sat_save_tools.utils import b64_bytes

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer

__all__ = ("StructProperty",)

logger = logging.getLogger(__name__)


class StructProperty(BaseProperty[StructValue | pydantic.Base64Bytes]):
    type_name: typing.Literal[PropertyTypeName.STRUCT] = PropertyTypeName.STRUCT
    index: int = 0
    type: StructTypeName
    unk1: pydantic.Base64Bytes = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"  # type: ignore

    def __serialize__(self, ser: Serializer) -> None:
        ns = ser.new()
        ns.add(self.value)

        ser.add_struct(
            String(self.name)
            | Object(self.type_name)
            | U32(len(ns))
            | U32(self.index)
            | Object(self.type)
            | Raw(len(self.unk1))(self.unk1)
            | Raw(len(ns.content))(ns.content),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            String("name")
            | Object(PropertyTypeName)("type_name")
            | U32("payload_size")
            | U32("index")
            | Object(StructTypeName)("type")
            | B64Raw(17)("unk1"),
        )

        with des.slice(content["payload_size"]) as sub_des:
            content |= sub_des.get_dict(
                Function(
                    deserialize_struct_value,
                    struct_type=content["type"],
                    payload_size=content["payload_size"],
                )("value"),
            )
        content["value"] = b64_bytes(content["value"])

        return cls.model_validate(content)
