import typing

type ParseErrorCode = typing.Literal[
    "context_not_provided",
    "corrupt_data",
    "invalid_deserializer",
    "invalid_flag",
    "invalid_size",
    "obj_is_not_deserializable",
    "obj_is_not_serializable",
    "string_decode_failure",
    "unk",
    "unsupported_version",
    "unknown_file_type",
    "map_markers_limit",
]


class SatisfactorySaveParserError(ValueError):
    code: ParseErrorCode
    message: str
    args: tuple[object, ...]

    @typing.overload
    def __init__(self, code: str, message: None = ..., *args: object) -> None: ...
    @typing.overload
    def __init__(self, code: ParseErrorCode, message: str, *args: object) -> None: ...

    def __init__(
        self,
        code: ParseErrorCode | str,
        message: str | None = None,
        *args: object,
    ) -> None:
        if message is None:
            msg = code.format(*args)
            code = "unk"
        else:
            msg = message.format(*args)
        super().__init__(msg)

        self.code = typing.cast("ParseErrorCode", code)
        self.message = msg
        self.args = args

    def __str__(self) -> str:
        return self.message.format(*self.args)

    def __repr__(self) -> str:
        code = self.code
        message = self.message.format(*self.args)
        return f"<ParseError {code=} {message=}>"
