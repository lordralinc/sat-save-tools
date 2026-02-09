import collections.abc
import contextlib
import logging
import struct
import typing

from sat_save_tools.const import TRACE_BIN_LOG_LEVEL
from sat_save_tools.exceptions import SatisfactorySaveParserError
from sat_save_tools.logger import get_struct_name, logging_with_context, repr_result
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
    "Deserializable",
    "DeserializeFn",
    "Deserializer",
)

logger: logging.Logger = logging.getLogger(__name__)

T = typing.TypeVar("T")
PS = typing.ParamSpec("PS")


@typing.runtime_checkable
class Deserializable(typing.Protocol):
    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self: ...


type DeserializeFn[T, **PS] = collections.abc.Callable[typing.Concatenate["Deserializer", PS], T]


class Deserializer(SerdeCtx):
    _struct_cache: typing.ClassVar[dict[str, struct.Struct]] = {}

    def __init__(
        self,
        content: bytearray | bytes | memoryview[bytes],
        offset: int | None = None,
        *,
        context: dict[str, typing.Any] | None = None,
    ) -> None:
        super().__init__(context=context)
        self._content = memoryview(bytes(content)) if not isinstance(content, memoryview) else content
        self.offset = offset or 0
        self.total = len(self._content)

    def __len__(self) -> int:
        return len(self._content)

    def new(self, content: bytearray | bytes | memoryview[bytes]) -> typing.Self:
        return self.__class__(
            content=content,
            offset=0,
            context=self.ctx.copy(),
        )

    @contextlib.contextmanager
    def slice(self, size: int):
        sub_des = self.new(self.get_raw(size))
        yield sub_des
        if sub_des.offset != len(sub_des):
            raise SatisfactorySaveParserError("invalid_deserializer", "Sub deserializer don't read all bytes")

    def copy(self) -> typing.Self:
        return self.__class__(
            content=self._content,
            offset=self.offset,
            context=self.ctx.copy(),
        )

    @property
    def content(self) -> memoryview[bytes]:
        return typing.cast("memoryview[bytes]", self._content)

    def get_raw(self, size: int) -> bytes:
        if self.offset + size > self.total:
            raise SatisfactorySaveParserError("invalid_deserializer", "Invalid raw size")
        with logging_with_context(struct=f"raw[{size}]", offset=self.offset, total=self.total):
            value = self.content[self.offset : self.offset + size]
            self.offset += size
            return bytes(value)

    def deserialize_fmt(self, fmt: str) -> tuple[typing.Any, ...]:
        st = self._struct_cache.setdefault(fmt, struct.Struct(fmt))
        with logging_with_context(struct=fmt, offset=self.offset, total=self.total):
            try:
                values = st.unpack_from(self._content, self.offset)
            except struct.error as exc:
                raise SatisfactorySaveParserError(
                    "corrupt_data",
                    "struct unpack failed at offset {:X}",
                    self.offset,
                ) from exc
            else:
                if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
                    logger.log(
                        TRACE_BIN_LOG_LEVEL,
                        "Get struct of['%X'->'%X'] '%s' | %s",
                        self.offset,
                        self.offset + st.size,
                        fmt,
                        repr_result(values),
                    )
                self.offset += st.size
                return values

    @typing.overload
    def get_struct(self, fmt: Struct | Field, *, first: typing.Literal[False] = ...) -> tuple[typing.Any, ...]: ...
    @typing.overload
    def get_struct(self, fmt: Struct | Field, *, first: typing.Literal[True] = ...) -> typing.Any: ...

    def get_struct(self, fmt: Struct | Field, *, first: bool = False) -> tuple[typing.Any, ...] | typing.Any:
        if isinstance(fmt, Field):
            fmt = fmt.as_struct()
        values = []
        seq = fmt.get_deserialize_seq()
        for seq_item in seq:
            if isinstance(seq_item, FmtSymbol):
                values.extend(self.deserialize_fmt(seq_item.fmt))
                continue
            if isinstance(seq_item, StringSymbol):
                values.append(self.get_string())
                continue
            if isinstance(seq_item, ObjectSymbol):
                values.append(self.get(seq_item.object_cls))
                continue
            if isinstance(seq_item, FunctionSymbol):
                values.append(self.get_fn(seq_item.function, *seq_item.args, **seq_item.kwargs))
                continue
        if first:
            return values[0]
        return tuple(values)

    def get_dict(self, fmt: Struct | Field) -> dict[str, typing.Any]:
        if isinstance(fmt, Field):
            fmt = fmt.as_struct()
        for it in fmt.fields:
            if it.name is None:
                raise ValueError(f"Field {it!r} on struct {fmt!r} does not have name.")
        values = list(self.get_struct(fmt))

        if len(values) != len(fmt.fields):
            raise ValueError("values is shorter than fields")

        for i in range(len(fmt.fields)):
            field = fmt.fields[i]
            if hasattr(field, "validator"):
                validator: collections.abc.Callable[[typing.Any], typing.Any] = getattr(field, "validator", lambda x: x)
                values[i] = validator(values[i])

        return typing.cast(
            "dict[str, typing.Any]",
            dict(zip([it.name for it in fmt.fields], values, strict=True)),
        )

    def get[T: Deserializable](self, item: type[T]) -> T:
        if not isinstance(item, Deserializable):
            raise SatisfactorySaveParserError(
                "obj_is_not_deserializable",
                "object {} is not impl SFSaveDeserializable protocol",
                get_struct_name(item),
            )
        with logging_with_context(struct=item, offset=self.offset, total=self.total):
            start = self.offset
            value = item.__deserialize__(self)

            if self.offset == start:
                if logger.isEnabledFor(logging.ERROR):
                    logger.error(
                        TRACE_BIN_LOG_LEVEL,
                        "Deserializer %r did not advance offset (%d)",
                        item,
                        start,
                    )
                raise SatisfactorySaveParserError(
                    "invalid_deserializer",
                    "Deserializer did not advance offset",
                )
            if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
                logger.log(
                    TRACE_BIN_LOG_LEVEL,
                    "GET of['%X'->'%X'] '%s' | '%s'",
                    start,
                    self.offset,
                    get_struct_name(item),
                    repr_result(value),
                )
            return value

    def get_fn[T, **PS](self, fn: DeserializeFn[T, PS], *args: PS.args, **kwargs: PS.kwargs) -> T:
        with logging_with_context(struct=fn, offset=self.offset, total=self.total):
            start_offset: int = self.offset
            value: T = fn(self, *args, **kwargs)
            if self.offset == start_offset:
                if logger.isEnabledFor(logging.ERROR):
                    logger.error(
                        "Deserializer %s did not advance offset (%d)",
                        get_struct_name(fn),
                        start_offset,
                    )
                raise SatisfactorySaveParserError(
                    "invalid_deserializer",
                    "Deserializer did not advance offset",
                )
            if logger.isEnabledFor(TRACE_BIN_LOG_LEVEL):
                logger.log(
                    TRACE_BIN_LOG_LEVEL,
                    "GET FUNCTION of['%X'->'%X'] '%s' | %r %r | '%s'",
                    start_offset,
                    self.offset,
                    get_struct_name(fn),
                    args,
                    kwargs,
                    repr_result(value),
                )
            return value

    def get_string(self) -> str:
        length, *_ = self.deserialize_fmt("<" + I32.fmt)

        if length == 0:
            return ""

        # UTF-16LE
        if length < 0:
            char_len: int = -length - 1
            byte_len: int = char_len * 2

            raw = self._content[self.offset : self.offset + byte_len]
            s: str = raw.tobytes().decode("utf-16-le").encode("utf-16", "surrogatepass").decode("utf-16")
            self.offset += byte_len + 2
            return s.replace("\x00", "")
        # UTF-8
        byte_len: int = length - 1
        raw = self._content[self.offset : self.offset + byte_len]
        s: str = raw.tobytes().decode("utf-8")
        self.offset += byte_len + 1

        return s.replace("\x00", "")
