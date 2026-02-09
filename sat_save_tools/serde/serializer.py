import collections
import collections.abc
import copy
import logging
import struct
import typing

from sat_save_tools.const import TRACE_BIN_LOG_LEVEL
from sat_save_tools.exceptions import SatisfactorySaveParserError
from sat_save_tools.logger import get_struct_name, logging_with_context
from sat_save_tools.serde.base import SerdeCtx
from sat_save_tools.serde.formats import (
    I32,
    Field,
    FmtSymbol,
    FunctionSymbol,
    ObjectSymbol,
    StringSymbol,
    Struct,
)

__all__ = (
    "Serializable",
    "SerializeFn",
    "Serializer",
)


logger: logging.Logger = logging.getLogger(__name__)


T = typing.TypeVar("T")
PS = typing.ParamSpec("PS")


@typing.runtime_checkable
class Serializable(typing.Protocol):
    def __serialize__(self, ser: "Serializer") -> None: ...


type SerializeFn[T, **PS] = collections.abc.Callable[typing.Concatenate["Serializer", T, PS], T]


class Serializer(SerdeCtx):
    _struct_cache: typing.ClassVar[dict[str, struct.Struct]] = {}

    def __init__(
        self,
        content: bytearray | bytes | memoryview | None = None,
        *,
        context: dict[str, typing.Any] | None = None,
    ) -> None:
        super().__init__(context=context)
        self._content = bytearray(content or b"")

    @property
    def content(self) -> bytes:
        return bytes(self._content)

    def __len__(self) -> int:
        return len(self._content)

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_raw(self._content)

    def new(self) -> typing.Self:
        return self.__class__(
            content=b"",
            context=self.ctx.copy(),
        )

    def copy(self) -> typing.Self:
        return self.__class__(
            content=copy.copy(self._content),
            context=self.ctx.copy(),
        )

    def add_raw(self, content: collections.abc.Buffer) -> None:
        self._content += content

    def serialize_fmt(self, fmt: str, *values: typing.Any) -> None:
        fmt = fmt if isinstance(fmt, str) else fmt.get()
        st = self._struct_cache.setdefault(fmt, struct.Struct(fmt))
        offset = len(self)
        self._content += b"\x00" * st.size

        try:
            st.pack_into(self._content, offset, *values)
        except struct.error as exc:
            raise SatisfactorySaveParserError(
                "corrupt_data",
                "struct pack failed at {}",
                fmt,
            ) from exc

    def add_struct(self, struct: Struct | Field) -> None:
        if isinstance(struct, Field):
            struct = struct.as_struct()
        seq = struct.get_serialize_seq()
        for symbol, value in seq:
            if isinstance(symbol, FmtSymbol):
                self.serialize_fmt(
                    symbol.fmt,
                    *value,
                )
            if isinstance(symbol, StringSymbol):
                self.add_string(value)  # type: ignore
            if isinstance(symbol, ObjectSymbol):
                self.add(value)  # type: ignore
            if isinstance(symbol, FunctionSymbol):
                self.add_fn(symbol.function, *symbol.args, **symbol.kwargs)  # type: ignore

    def add(self, value: Serializable | bytes | bytearray | memoryview) -> typing.Self:
        if isinstance(value, (bytes, bytearray, memoryview)):
            self.add_raw(value)
            return self
        with logging_with_context(struct=value):
            if not isinstance(value, Serializable):
                raise SatisfactorySaveParserError(
                    "obj_is_not_serializable",
                    "object {} is not impl SFSaveSerializable protocol",
                    get_struct_name(value),
                )
            if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
                logger.log(TRACE_BIN_LOG_LEVEL, "serialize object %s", get_struct_name(value))
            before: int = len(self.content)
            value.__serialize__(self)
            if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
                logger.log(
                    TRACE_BIN_LOG_LEVEL,
                    "serialize object %s done: +%d bytes",
                    get_struct_name(value),
                    len(self.content) - before,
                )
            return self

    def add_fn[T, **PS](self, fn: SerializeFn[T, PS], obj: T, *args: PS.args, **kwargs: PS.kwargs) -> typing.Self:
        if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
            logger.log(TRACE_BIN_LOG_LEVEL, "serialize fn %s(%r)", fn.__qualname__, obj)
        before: int = len(self.content)
        fn(self, obj, *args, **kwargs)
        if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
            logger.log(
                TRACE_BIN_LOG_LEVEL,
                "serialize fn %s done: +%d bytes",
                fn.__qualname__,
                len(self.content) - before,
            )
        return self

    def add_string(self, value: str) -> typing.Self:
        with logging_with_context(struct=value):
            if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
                logger.log(TRACE_BIN_LOG_LEVEL, "add_string %r", value)

            if not value:
                self.serialize_fmt(I32.fmt, 0)
                return self

            try:
                encoded: bytes = value.encode("utf-8")
                length: int = len(encoded) + 1
                if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
                    logger.log(TRACE_BIN_LOG_LEVEL, "string utf-8 bytes=%d", length)
                self._content += struct.pack("<i", length) + encoded + b"\x00"
            except UnicodeEncodeError:
                encoded: bytes = value.encode("utf-16-le")
                char_count: int = (len(encoded) // 2) + 1
                if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
                    logger.log(TRACE_BIN_LOG_LEVEL, "string utf-16 chars=%d", char_count)
                self._content += struct.pack("<i", -char_count) + encoded + b"\x00\x00"

            return self
