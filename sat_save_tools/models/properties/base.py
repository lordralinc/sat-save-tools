import typing

import pydantic

from sat_save_tools.utils import pydantic_eq

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializer

__all__ = ("BaseProperty",)


@pydantic_eq
class BaseProperty[T](pydantic.BaseModel):
    name: str
    value: T

    def __serialize__(self, ser: "Serializer") -> None:
        raise NotImplementedError

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        raise NotImplementedError
