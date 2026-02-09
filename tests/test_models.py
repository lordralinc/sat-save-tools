import typing

import pytest

from sat_save_tools.logger import get_struct_name
from sat_save_tools.models import (
    ActorObject,
    BlueprintGameModeTrailingContainer,
    ComponentHeader,
    ComponentObject,
    ConveyorTrailing,
    ConveyorTrailingContainer,
    GridName,
    Level,
    LevelGroupingGrid,
    LevelInfo,
    SaveFileBody,
    SaveFileHeader,
    SaveFileHeaderFlags,
    deserialize_object_header,
)
from sat_save_tools.models.object_header import ActorHeader
from sat_save_tools.serde import Deserializable, Deserializer, Serializable, Serializer
from sat_save_tools.utils import b64_bytes
from tests.data import FLOAT_QUATERNION, FLOAT_VECTOR_3, OBJECT_REFERENCE, PROPERTY_LIST

header = SaveFileHeader(
    header_version=14,
    save_version=52,
    build_version=463028,
    save_name="save_name",
    map_name="Persistent_Level",
    map_options="?ClientIdentity=00?Visibility=SV_FriendsOnly",
    session_name="save",
    play_duration=124668,
    save_ticks=639029655211049984,
    flags=SaveFileHeaderFlags.FRIENDS_ONLY,
    editor_object_version=40,
    mod_metadata="",
    mod_flags=0,
    save_id="kdi3ik3sYg9zZsOsfXwruW",
    is_partitioned_world=True,
    creative_mode_enabled=True,
    checksum="/vJzWTXlOKCpOzU5Z8lpqA==",  # type: ignore
    is_cheat=False,
)
level_info = LevelInfo(name="LevelInfo.name", value=103)
level_grouping_grid = LevelGroupingGrid(
    name=GridName.MAIN,
    hex=0,
    count=1,
    levels=[level_info],
)


conveyor_trailing = ConveyorTrailing(
    length=1,
    name="ConveyorTrailing.name",
    unk1="ConveyorTrailing.unk1",
    unk2="ConveyorTrailing.unk2",
    postition=3.1434,
)
conveyor_trailing_container = ConveyorTrailingContainer(
    items=[conveyor_trailing, conveyor_trailing, conveyor_trailing],
)
blueprint_game_mode_trailing_container = BlueprintGameModeTrailingContainer(items=[OBJECT_REFERENCE])

actor_header = ActorHeader(
    type_path="ActorHeader.type_path",
    root_object="ActorHeader.root_object",
    instance_name="ActorHeader.instance_name",
    unknown=0,
    rotation=FLOAT_QUATERNION,
    position=FLOAT_VECTOR_3,
    scale=FLOAT_VECTOR_3,
    need_transform=False,
    was_placed_in_level=True,
)
actor_object = ActorObject(
    header=actor_header,
    save_version=52,
    flag=0,
    parent_object_reference=OBJECT_REFERENCE,
    components=[OBJECT_REFERENCE],
    properties=PROPERTY_LIST,
    trailing=b64_bytes(b""),
)
component_header = ComponentHeader(
    type_path="ComponentHeader.type_path",
    root_object="ComponentHeader.root_object",
    instance_name="ComponentHeader.instance_name",
    unknown=0,
    parent_actor_name="ComponentHeader.parent_actor_name",
)
component_object = ComponentObject(
    header=component_header,
    save_version=52,
    flag=0,
    properties=PROPERTY_LIST,
    trailing=b64_bytes(b""),
)

not_persistent_level = Level(
    name="Level.name",
    collectables=[OBJECT_REFERENCE],
    objects={
        actor_object.header.instance_name: actor_object,
        component_object.header.instance_name: component_object,
    },
    save_version=52,
    second_collectables=[OBJECT_REFERENCE],
)
persistent_level = Level(
    extra_level_name="Level.extra_level_name",
    collectables=[OBJECT_REFERENCE],
    objects={
        actor_object.header.instance_name: actor_object,
        component_object.header.instance_name: component_object,
    },
)
file_body = SaveFileBody(
    partition_count=6,
    hex_1=0,
    hex_2=0,
    grids=[
        level_grouping_grid,
        level_grouping_grid,
        level_grouping_grid,
        level_grouping_grid,
        level_grouping_grid,
    ],
    levels=[not_persistent_level, not_persistent_level],
    persistent_level=persistent_level,
)

ITEMS = (
    header,
    conveyor_trailing,
    conveyor_trailing_container,
    level_info,
    level_grouping_grid,
    blueprint_game_mode_trailing_container,
    file_body,
)


@pytest.mark.parametrize(
    ("item_cls", "item"),
    [(item.__class__, item) for item in ITEMS],
    ids=(f"serde {get_struct_name(item.__class__)}" for item in ITEMS),
)
def test_models_serde[T](item_cls: type[T], item: T):
    ser = Serializer().ctx_update(header=header)
    ser.add(typing.cast("Serializable", item))
    calculated = Deserializer(ser.content).ctx_update(header=header).get(typing.cast("Deserializable", item_cls))  # type: ignore
    assert calculated == item


def test_serde_actor():
    ser = Serializer()
    ser.add(actor_header)
    calculated = Deserializer(ser.content).get_fn(deserialize_object_header)
    assert calculated == actor_header

    ser = Serializer().ctx_update(header=header, level_object_header=actor_header)
    ser.add(actor_object)
    calculated = Deserializer(ser.content).ctx_update(header=header, level_object_header=actor_header).get(ActorObject)
    assert calculated == actor_object


def test_serde_component():
    ser = Serializer()
    ser.add(component_header)
    calculated = Deserializer(ser.content).get_fn(deserialize_object_header)
    assert calculated == component_header

    ser = Serializer().ctx_update(header=header, level_object_header=component_header)
    ser.add(component_object)
    calculated = (
        Deserializer(ser.content)
        .ctx_update(
            header=header,
            level_object_header=component_header,
        )
        .get(ComponentObject)
    )
    assert calculated == component_object


def test_levels():
    ser = Serializer()
    ser.ctx_update(header=header, is_persistent=True).add(persistent_level)
    calculated = Deserializer(ser.content).ctx_update(header=header, is_persistent=True).get(Level)
    assert calculated == persistent_level

    ser = Serializer()
    ser.ctx_update(header=header, is_persistent=False).add(not_persistent_level)
    calculated = Deserializer(ser.content).ctx_update(header=header, is_persistent=False).get(Level)
    assert calculated == not_persistent_level
