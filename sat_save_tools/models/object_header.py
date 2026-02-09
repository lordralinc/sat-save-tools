import enum
import typing

import pydantic

from sat_save_tools.logger import set_struct_name
from sat_save_tools.models.properties.typed_data import FloatQuaternion, FloatVector3
from sat_save_tools.models.save_file_header import U32Bool
from sat_save_tools.serde import U32, Object, String
from sat_save_tools.utils import (
    U32EnumDeserializerMixin,
    U32EnumSerializerMixin,
    pydantic_eq,
)

if typing.TYPE_CHECKING:
    from sat_save_tools.serde import Deserializer, Serializer

__all__ = (
    "ActorHeader",
    "ComponentHeader",
    "HeaderType",
    "ObjectHeaderType",
    "deserialize_object_header",
)


class HeaderType(U32EnumSerializerMixin, U32EnumDeserializerMixin, enum.IntEnum):
    COMPONENT = 0
    ACTOR = 1


@pydantic_eq
class ActorHeader(pydantic.BaseModel):
    type: typing.Literal[HeaderType.ACTOR] = HeaderType.ACTOR
    type_path: typing.Annotated[
        str,
        pydantic.Field(
            title="Type Path",
            description="The type of actor, described in a hierarchical path",
        ),
    ]
    root_object: typing.Annotated[
        str,
        pydantic.Field(title="Root Object"),
    ]
    instance_name: typing.Annotated[
        str,
        pydantic.Field(title="Instance Name", description="The unique name of this actor object"),
    ]
    unknown: typing.Annotated[
        int,
        pydantic.Field(title="Unknown Uint32"),
    ]
    rotation: FloatQuaternion
    position: FloatVector3
    scale: FloatVector3

    need_transform: typing.Annotated[
        bool,
        pydantic.Field(
            title="Need Transform?",
            description="Seemingly a boolean flag; semantics unclear",
        ),
    ]

    was_placed_in_level: typing.Annotated[
        bool,
        pydantic.Field(
            title="Was Placed In Level?",
            description="Seemingly a boolean flag; semantics unclear",
        ),
    ]

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            Object(self.type)
            | String(self.type_path)
            | String(self.root_object)
            | String(self.instance_name)
            | U32(self.unknown)
            | U32Bool(self.need_transform)
            | Object(self.rotation)
            | Object(self.position)
            | Object(self.scale)
            | U32Bool(self.was_placed_in_level),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("type_path")
                | String("root_object")
                | String("instance_name")
                | U32("unknown")
                | U32Bool("need_transform")
                | Object(FloatQuaternion)("rotation")
                | Object(FloatVector3)("position")
                | Object(FloatVector3)("scale")
                | U32Bool("was_placed_in_level"),
            ),
        )


@pydantic_eq
class ComponentHeader(pydantic.BaseModel):
    type: typing.Literal[HeaderType.COMPONENT] = HeaderType.COMPONENT
    type_path: typing.Annotated[
        str,
        pydantic.Field(
            title="Type Path",
            description="The type of component, described in a hierarchical path",
        ),
    ]
    root_object: typing.Annotated[
        str,
        pydantic.Field(title="Root Object"),
    ]
    instance_name: typing.Annotated[
        str,
        pydantic.Field(
            title="Instance Name",
            description="the name of this single component object ",
        ),
    ]
    unknown: typing.Annotated[
        int,
        pydantic.Field(title="Unknown Uint32"),
    ]
    parent_actor_name: typing.Annotated[
        str,
        pydantic.Field(
            title="parent actor name",
            description="a reference to the instance name of an actor",
        ),
    ]

    def __serialize__(self, ser: "Serializer") -> None:
        ser.add_struct(
            Object(self.type)
            | String(self.type_path)
            | String(self.root_object)
            | String(self.instance_name)
            | U32(self.unknown)
            | String(self.parent_actor_name),
        )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        return cls.model_validate(
            des.get_dict(
                String("type_path")
                | String("root_object")
                | String("instance_name")
                | U32("unknown")
                | String("parent_actor_name"),
            ),
        )


type ObjectHeaderType = typing.Annotated[
    ActorHeader | ComponentHeader,
    pydantic.Field(discriminator="type"),
]


@set_struct_name("ObjectHeader")
def deserialize_object_header(des: "Deserializer") -> ObjectHeaderType:
    header_type = des.get(HeaderType)
    if header_type == HeaderType.COMPONENT:
        return des.get(ComponentHeader)
    if header_type == HeaderType.ACTOR:
        return des.get(ActorHeader)
    typing.assert_never(header_type)
