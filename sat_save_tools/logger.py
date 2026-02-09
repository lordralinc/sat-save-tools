import collections
import collections.abc
import contextlib
import contextvars
import functools
import inspect
import logging
import typing

from sat_save_tools.const import TRACE_BIN_LOG_LEVEL
from sat_save_tools.env import SF_LOGS_ENABLE_OFFSET, SF_LOGS_ENABLE_STRUCT_PATHS

__all__ = (
    "ContextFilter",
    "logging_with_context",
)


logging.addLevelName(TRACE_BIN_LOG_LEVEL, "TRACE_BIN")
logger = logging.getLogger()


class _LogContext(typing.TypedDict):
    structs: typing.NotRequired[list]
    offset: typing.NotRequired[int]
    total: typing.NotRequired[int]


_log_context: contextvars.ContextVar[_LogContext] = contextvars.ContextVar(
    "log_context",
    default=_LogContext(),  # noqa: B039
)

PS = typing.ParamSpec("PS")
R = typing.TypeVar("R")


def set_struct_name(
    name: str,
) -> collections.abc.Callable[
    [collections.abc.Callable[PS, R]],
    collections.abc.Callable[PS, R],
]:
    def wrapper(fn: collections.abc.Callable[PS, R]) -> collections.abc.Callable[PS, R]:
        setattr(fn, "__struct_name__", name)  # noqa: B010
        return fn

    return wrapper


def get_struct_name(  # noqa: PLR0911
    item: str | typing.Callable | functools.partial | typing.Any,
) -> str:
    if isinstance(item, str) and item.startswith("<"):
        return f"[{item}]"
    if hasattr(item, "__struct_name__"):
        return item.__struct_name__  # type: ignore

    if isinstance(item, str):
        return item
    if isinstance(item, functools.partial):
        return get_struct_name(item.func)
    if inspect.isclass(item):
        return item.__name__

    if hasattr(item, "__qualname__"):
        return item.__qualname__
    if hasattr(item, "__name__"):
        return item.__name__
    if hasattr(item, "__class__"):
        return get_struct_name(item.__class__)
    return repr(item)


def repr_result(result: typing.Any) -> str:
    if isinstance(result, bytes):
        return result.hex(" ")
    return repr(result)


@contextlib.contextmanager
def logging_with_context(**kwargs: typing.Any):
    current = _log_context.get()
    merged = current.copy()
    structs_backup = current.get("structs", []).copy()

    if "structs" not in merged:
        merged["structs"] = []

    for k, v in kwargs.items():
        if k == "struct":
            merged["structs"].append(v)
        else:
            merged[k] = v
    _log_context.set(merged)
    try:
        yield
    finally:
        ctx = _log_context.get()
        ctx["structs"] = structs_backup
        for k in kwargs:
            if k != "struct":
                ctx.pop(k, None)
        _log_context.set(ctx)


class ContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        context = _log_context.get()
        record._ctx = context  # noqa: SLF001
        record.context = ""

        ctx_args = []
        if SF_LOGS_ENABLE_STRUCT_PATHS:
            ctx_args.append(
                "struct='" + ".".join(get_struct_name(it) for it in context.get("structs", [])) + "'",
            )
        if SF_LOGS_ENABLE_OFFSET and context.get("offset"):
            offset = context.get("offset", 0)
            total = context.get("total", None)

            if total:
                ctx_args.append(
                    f"progress={offset:#X}/{total:#X} ({offset / total:.2%})",
                )
            else:
                ctx_args.append(f"offset={offset:#X}")
        if context:
            if ctx_args or ({k for k in context if k not in ("structs", "total", "offset")}):
                record.context = "[{}]".format(
                    " ".join(ctx_args)
                    + " ".join(
                        [f"{k}='{v}'" for k, v in context.items() if k not in ("structs", "total", "offset")],
                    ),
                )
        else:
            record.context = ""
        return True
