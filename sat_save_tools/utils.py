import base64
import collections
import collections.abc
import math
import typing
from contextlib import contextmanager

import pydantic

from .exceptions import SatisfactorySaveParserError
from .serde import U8, U32, Deserializer, Serializer, String

__all__ = (
    "StrEnumDeserializerMixin",
    "StrEnumSerializerMixin",
    "U8EnumDeserializerMixin",
    "U8EnumSerializerMixin",
    "U32EnumDeserializerMixin",
    "U32EnumSerializerMixin",
    "expect_size",
    "make_chunks",
    "require",
)


@contextmanager
def expect_size(p: Deserializer, size: int, what: str):
    start = p.offset
    yield
    diff = p.offset - start
    if diff != size:
        raise SatisfactorySaveParserError("invalid_size", f"{what}: invalid size {diff}, expected {size}")


class StrEnumSerializerMixin:
    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_string(self)  # type: ignore


class StrEnumDeserializerMixin:
    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        value, *_ = des.get_struct(String())
        return cls(value)  # type: ignore


class U8EnumSerializerMixin:
    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U8(self))  # type: ignore


class U8EnumDeserializerMixin:
    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        value, *_ = des.get_struct(U8)
        return cls(value)  # type: ignore


class U32EnumSerializerMixin:
    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(U32(self))  # type: ignore


class U32EnumDeserializerMixin:
    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        value, *_ = des.get_struct(U32)
        return cls(value)  # type: ignore


def b64_bytes[T](v: T) -> T:
    if isinstance(v, (bytes, bytearray, memoryview)):
        return base64.b64encode(bytes(v)).decode("ascii")  # type: ignore
    return v


def float_eq[T](
    float_slots: collections.abc.Iterable[str] = (),
    double_slots: collections.abc.Iterable[str] = (),
    other_slots: collections.abc.Iterable[str] = (),
    abs_tol: float = 1e-12,
) -> collections.abc.Callable[[type[T]], type[T]]:
    def wrapper(_cls: type[T]) -> type[T]:
        def __eq__(self: T, other: object) -> bool:  # noqa: N807
            if not isinstance(other, _cls):
                return NotImplemented

            for slot, rel_tol in (
                *((s, 1e-6) for s in float_slots),
                *((s, 1e-9) for s in double_slots),
            ):
                a = getattr(self, slot)
                b = getattr(other, slot)

                if a is None or b is None:
                    if a is b:
                        continue
                    return False
                if not math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol):
                    return False
            return all(getattr(self, slot) == getattr(other, slot) for slot in other_slots)

        setattr(_cls, "__eq__", __eq__)  # noqa: B010
        setattr(_cls, "__hash__", None)  # noqa: B010
        return _cls

    return wrapper


def pydantic_eq[T: pydantic.BaseModel](_cls: type[T]) -> type[T]:
    def __eq__(self: T, other: typing.Any) -> bool:  # noqa: N807
        if not isinstance(other, self.__class__):
            return NotImplemented
        for field in self.__class__.model_fields:
            val_self = getattr(self, field)
            val_other = getattr(other, field)
            if val_self != val_other:
                return False
        return True

    _cls.__eq__ = __eq__
    return _cls


def make_chunks(
    data: "bytes | memoryview[bytes]",
    max_size: int,
) -> "collections.abc.Iterator[memoryview[bytes]]":
    mv = data if isinstance(data, memoryview) else memoryview(data)
    size = len(mv)

    offset = 0
    while offset < size:
        end = min(offset + max_size, size)
        yield typing.cast("memoryview[bytes]", mv[offset:end])
        offset = end


def require[T](v: T | None) -> T:
    if v is None:
        raise ValueError("Value is None")
    return v
