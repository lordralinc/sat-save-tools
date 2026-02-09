import collections
import collections.abc
import copy
import functools
import inspect
import typing
from base64 import b64encode

from sat_save_tools.exceptions import SatisfactorySaveParserError
from sat_save_tools.logger import get_struct_name

if typing.TYPE_CHECKING:
    from sat_save_tools.serde.deserializer import Deserializable, DeserializeFn
__all__ = (
    "I8",
    "I32",
    "I64",
    "U8",
    "U32",
    "U64",
    "Double",
    "Float",
    "Function",
    "Object",
    "Primitive",
    "Raw",
    "String",
    "Struct",
    "U8Bool",
    "U32Bool",
)


type DeserializeSequence = list[
    typing.Union[  # noqa: UP007
        "FmtSymbol",
        "StringSymbol",
        "ObjectSymbol",
        "FunctionSymbol",
    ]
]

type SerialzieSequence = list[
    typing.Union[  # noqa: UP007
        tuple["FmtSymbol", tuple[typing.Any, ...]],
        tuple["StringSymbol", str],
        tuple["ObjectSymbol", typing.Any],
        tuple["FunctionSymbol", typing.Any],
    ]
]


class Struct:
    __slots__ = ("fields",)

    def __init__(self, fields: "list[Field]") -> None:
        self.fields = fields

    def __or__(self, other: "Field | typing.Self") -> typing.Self:
        return self.__class__(
            [
                *self.fields,
                *([other] if isinstance(other, Field) else other.fields),
            ],
        )

    def __mul__(self, other: int) -> typing.Self:
        last_element = self.fields[-1]
        return self.__class__([*self.fields[:-1], *(last_element * other).fields])

    def get_deserialize_seq(self) -> DeserializeSequence:
        current_format = ""
        seq = []
        for field in self.fields:
            if isinstance(field, Primitive):
                current_format += field.fmt
                continue
            if current_format:
                seq.append(FmtSymbol(f"<{current_format}"))
                current_format = ""

            if isinstance(field, (Raw, B64Raw)):
                current_format += f"{field.bytes_len}s"
                continue
            if isinstance(field, String):
                seq.append(StringSymbol())

            if isinstance(field, Object):
                seq.append(
                    ObjectSymbol(
                        (
                            field.object_cls_or_value
                            if inspect.isclass(field.object_cls_or_value)
                            else type(field.object_cls_or_value)
                        ),
                    ),
                )
            if isinstance(field, Function):
                seq.append(FunctionSymbol(field.function, *field.args, **field.kwargs))
        if current_format:
            seq.append(FmtSymbol(f"<{current_format}"))
            current_format = ""
        return seq

    def get_serialize_seq(
        self,
    ) -> SerialzieSequence:
        current_format = ""
        current_fmt_args = list()
        seq: SerialzieSequence = []
        for field in self.fields:
            if isinstance(field, Primitive):
                current_format += field.fmt
                current_fmt_args.append(field.content)
                continue

            if current_format:
                seq.append((FmtSymbol(f"<{current_format}"), tuple(current_fmt_args)))
                current_format = ""
                current_fmt_args = []

            if isinstance(field, (Raw, B64Raw)):
                current_format += f"{field.bytes_len}s"
                current_fmt_args.append(field.content)
                continue
            if isinstance(field, String):
                seq.append((StringSymbol(), typing.cast("str", field.content)))

            if isinstance(field, Object):
                seq.append(
                    (
                        ObjectSymbol(
                            (
                                field.object_cls_or_value
                                if inspect.isclass(field.object_cls_or_value)
                                else type(field.object_cls_or_value)
                            ),
                        ),
                        field.content,
                    ),
                )
            if isinstance(field, Function):
                seq.append(
                    (
                        FunctionSymbol(field.function, *field.args, **field.kwargs),
                        field.content,
                    ),
                )
        if current_format:
            current_format = f"<{current_format}"
            seq.append((FmtSymbol(current_format), tuple(current_fmt_args)))
            current_format = ""
        return seq

    @classmethod
    def from_iter[T](cls, it: "Field[T] | type[Field[T]]", _iter: collections.abc.Iterable[T]) -> "Struct":
        return functools.reduce(lambda a, b: a | b, [it(t) for t in _iter], Struct([]))  # type: ignore


class FmtSymbol:
    def __init__(self, fmt: str) -> None:
        self.fmt = fmt


class StringSymbol: ...


class ObjectSymbol[T: "Deserializable"]:
    def __init__(self, object_cls: type[T]) -> None:
        self.object_cls = object_cls


class FunctionSymbol[T, **PS]:
    def __init__(self, function: "DeserializeFn[T, PS]", *args: PS.args, **kwargs: PS.kwargs) -> None:
        self.function = function
        self.args = args
        self.kwargs = kwargs


class Field[T = typing.Any]:
    name: str | None = None
    content: T | None = None

    def __init__(self) -> None:
        self.name = None
        self.content = None

    def as_struct(self) -> Struct:
        return Struct([self])

    def __or__(self, other: "Field | Struct") -> Struct:
        return Struct(
            [
                self,
                *([other] if isinstance(other, Field) else other.fields),
            ],
        )

    def __mul__(self, other: int) -> Struct:
        if not isinstance(other, int):
            return NotImplemented
        if other < 1:
            return Struct([])
        return functools.reduce(lambda a, b: a | b, [copy.copy(self) for _ in range(other)], Struct([]))

    def __repr__(self) -> str:
        ctx = {}
        if self.name:
            ctx["name"] = self.name
        if self.content:
            ctx["content"] = repr(self.content)
        return "<{} at {:X} {}>".format(
            get_struct_name(self),
            id(self),
            " ".join(f"{k}={v}" for k, v in ctx.items()),
        )


class NameValueFieldMixin[T]:
    name: str | None
    content: T | None

    def __call__(self, name_or_content: str | T) -> typing.Self:
        self_c = copy.copy(self)
        if isinstance(name_or_content, str):
            self_c.name = name_or_content
        else:
            self_c.content = name_or_content
        if isinstance(self_c, String):
            self_c.content = name_or_content  # type: ignore
        return self_c


class Primitive[T](Field[T], NameValueFieldMixin[T]):
    def __init__(self, fmt: str, validator: typing.Callable[[typing.Any], T]) -> None:
        super().__init__()
        self.fmt = fmt
        self.validator = validator

    def __repr__(self) -> str:
        ctx = {}
        if self.name:
            ctx["name"] = self.name
        if self.content:
            ctx["content"] = repr(self.content)
        return "<{}[{}] at {:X}{}>".format(
            get_struct_name(self),
            self.fmt,
            id(self),
            "".join(f" {k}={v}" for k, v in ctx.items()),
        )


class String(Field[str], NameValueFieldMixin[str]):
    name: str | None
    content: str | None

    def __init__(self, name_or_content: str | None = None) -> None:
        super().__init__()
        self.name = name_or_content
        self.content = name_or_content

    def __repr__(self) -> str:
        ctx = {}
        if self.name:
            ctx["name"] = self.name
        if self.content:
            ctx["content"] = repr(self.content)
        return "<{} at {:X}{}>".format(
            get_struct_name(self),
            id(self),
            "".join(f" {k}={v}" for k, v in ctx.items()),
        )


class Raw(Field[bytes], NameValueFieldMixin[bytes]):
    def __init__(self, bytes_len: int) -> None:
        super().__init__()
        self.bytes_len = bytes_len

    def __repr__(self) -> str:
        ctx = {}
        if self.name:
            ctx["name"] = self.name
        if self.content:
            ctx["content"] = repr(self.content)
        return "<{} at {:X} {}>".format(
            get_struct_name(self),
            id(self),
            " ".join(f"{k}={v}" for k, v in ctx.items()),
        )

    @classmethod
    def with_len(cls, content: "bytes | memoryview[bytes]") -> Struct:
        length = len(content)
        return U32(length) | Raw(length)(bytes(content))


class B64Raw(Field[str], NameValueFieldMixin[str]):
    def __init__(self, bytes_len: int) -> None:
        super().__init__()
        self.bytes_len = bytes_len

    def validator(self, content: typing.Any) -> str:
        return b64encode(content).decode("ascii")

    def __call__(self, name_or_content: str | bytes) -> typing.Self:
        self_c = copy.copy(self)
        if isinstance(name_or_content, str):
            self_c.name = name_or_content
        elif isinstance(name_or_content, str):
            self_c.content = name_or_content
        else:
            self_c.content = b64encode(name_or_content).decode("ascii")  # type: ignore
        if isinstance(self_c, String):
            self_c.content = name_or_content  # type: ignore
        return self_c

    def __repr__(self) -> str:
        ctx = {}
        if self.name:
            ctx["name"] = self.name
        if self.content:
            ctx["content"] = repr(self.content)
        return "<{} at {:X} {}>".format(
            get_struct_name(self),
            id(self),
            " ".join(f"{k}={v}" for k, v in ctx.items()),
        )


class Object[T: "Deserializable"](Field[T], NameValueFieldMixin[T]):
    def __init__(self, object_cls_or_value: type[T] | T) -> None:
        super().__init__()
        self.object_cls_or_value = object_cls_or_value
        if not inspect.isclass(self.object_cls_or_value):
            self.content = object_cls_or_value

    def __repr__(self) -> str:
        ctx = {}
        if self.name:
            ctx["name"] = self.name
        if self.content:
            ctx["content"] = repr(self.content)
        return "<{}[{}] at {:X}{}>".format(
            get_struct_name(self),
            get_struct_name(self.object_cls_or_value),
            id(self),
            "".join(f" {k}={v}" for k, v in ctx.items()),
        )


class Function[T, **PS](Field[T], NameValueFieldMixin[T]):
    def __init__(self, function: "DeserializeFn[T, PS]", *args: PS.args, **kwargs: PS.kwargs) -> None:
        super().__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __repr__(self) -> str:
        ctx = {}
        if self.name:
            ctx["name"] = self.name
        if self.content:
            ctx["content"] = repr(self.content)
        return "<{}[{}] at {:X}{}>".format(
            get_struct_name(self),
            get_struct_name(self.function),
            id(self),
            "".join(f" {k}={v}" for k, v in ctx.items()),
        )


def _verify_bool(x: typing.Any) -> bool:
    value = int(x)
    if value not in (0, 1):
        raise SatisfactorySaveParserError("corrupt_data", "Invalid bool {}", value)
    return bool(value)


I8 = Primitive("b", int)
I32 = Primitive("i", int)
I64 = Primitive("q", int)
U8 = Primitive("B", int)
U32 = Primitive("I", int)
U64 = Primitive("Q", int)
Float = Primitive("f", float)
Double = Primitive("d", float)
U8Bool = Primitive(U8.fmt, _verify_bool)
U32Bool = Primitive(U32.fmt, _verify_bool)
