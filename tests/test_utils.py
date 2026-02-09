import enum

import pytest

from sat_save_tools.exceptions import SatisfactorySaveParserError
from sat_save_tools.serde import (
    U32,
    Deserializable,
    Deserializer,
    Serializable,
    Serializer,
)
from sat_save_tools.utils import (
    StrEnumDeserializerMixin,
    StrEnumSerializerMixin,
    U8EnumDeserializerMixin,
    U8EnumSerializerMixin,
    U32EnumDeserializerMixin,
    U32EnumSerializerMixin,
    expect_size,
)


class MyStrEnum(StrEnumSerializerMixin, StrEnumDeserializerMixin, enum.StrEnum):
    HELLO = "hello"
    WORLD = "world"


class MyU8Enum(U8EnumSerializerMixin, U8EnumDeserializerMixin, enum.IntEnum):
    A = 1
    B = 255


class MyU32Enum(U32EnumSerializerMixin, U32EnumDeserializerMixin, enum.IntEnum):
    X = 123456
    Y = 654321


def test_expect_size():
    size = 4
    content = b"\x00\x00\x00\x31\x00\x00\x00\x00"

    des = Deserializer(content)

    with expect_size(des, size, "test"):
        des.get_struct(U32)

    des = Deserializer(content)

    with pytest.raises(SatisfactorySaveParserError), expect_size(des, size - 1, "test"):
        des.get_struct(U32)


@pytest.mark.parametrize(
    ("enum_value", "bytes_value"),
    [
        (MyStrEnum.HELLO, b"\x06\x00\x00\x00hello\x00"),
        (MyU8Enum.B, b"\xff"),
        (MyU32Enum.Y, b"\xf1\xfb\t\x00"),
    ],
    ids=(
        "serialize str enum",
        "serialize u8 enum",
        "serialize u32 enum",
    ),
)
def test_enum_serialize(enum_value: Serializable, bytes_value: bytes):
    ser = Serializer()
    ser.add(enum_value)
    assert ser.content == bytes_value


@pytest.mark.parametrize(
    ("bytes_value", "enum_cls", "enum_value"),
    [
        (
            b"\x06\x00\x00\x00hello\x00",
            MyStrEnum,
            MyStrEnum.HELLO,
        ),
        (
            b"\xff",
            MyU8Enum,
            MyU8Enum.B,
        ),
        (
            b"\xf1\xfb\t\x00",
            MyU32Enum,
            MyU32Enum.Y,
        ),
    ],
    ids=(
        "deserialize str enum",
        "deserialize u8 enum",
        "deserialize u32 enum",
    ),
)
def test_enum_deserialize[T: Deserializable](
    bytes_value: bytes,
    enum_cls: type[T],
    enum_value: T,
):
    des = Deserializer(bytes_value)
    calc_enum_value = des.get(enum_cls)
    assert calc_enum_value == enum_value
