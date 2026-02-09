import typing

from sat_save_tools.exceptions import SatisfactorySaveParserError

__all__ = ("SerdeCtx",)


class SerdeCtx:
    ctx: dict[str, typing.Any]

    def __init__(self, *, context: dict[str, typing.Any] | None = None) -> None:
        self.ctx = context or {}

    def ctx_update(self, **kwargs: typing.Any) -> typing.Self:
        self.ctx.update(kwargs)
        return self

    def ctx_get(self, key: str) -> typing.Any:
        value = self.ctx.get(key)
        if value is None:
            raise SatisfactorySaveParserError("context_not_provided", "{} not found in context", key)
        return value
