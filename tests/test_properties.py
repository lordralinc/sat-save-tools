import copy
import time
import typing
import uuid

import pytest

from sat_save_tools import Deserializable, Deserializer, Serializable, Serializer
from sat_save_tools.logger import get_struct_name
from sat_save_tools.models.properties import PropertyList
from sat_save_tools.models.properties.array import StructTypeName
from sat_save_tools.models.properties.map import KeyTypeName, MapProperty, ValueTypeName
from sat_save_tools.models.properties.set import SetProperty, SetType
from sat_save_tools.models.properties.simple_preperties import (
    BoolProperty,
    ByteProperty,
    DoubleProperty,
    EnumProperty,
    FloatProperty,
    Int8Property,
    Int64Property,
    IntProperty,
    NameProperty,
    ObjectProperty,
    SoftObjectProperty,
    StrProperty,
    UInt32Property,
)
from sat_save_tools.models.properties.struct import StructProperty
from sat_save_tools.models.properties.text import TextValueBase
from sat_save_tools.models.properties.typed_data import (
    Box,
    ClientIdentityInfo,
    ClientIdentityInfoIdentity,
    ClientIdentityInfoIdentityVariant,
    DateTime,
    DoubleQuaternion,
    DoubleVector3,
    FluidBox,
    InventoryItem,
    LinearColor,
    RailroadTrackPosition,
    SpawnData,
)
from sat_save_tools.utils import b64_bytes

from .data import (
    ARRAY_ELEMENT_BYTE,
    ARRAY_ELEMENT_ENUM,
    ARRAY_ELEMENT_FLOAT,
    ARRAY_ELEMENT_INT,
    ARRAY_ELEMENT_INT64,
    ARRAY_ELEMENT_INTERFACE,
    ARRAY_ELEMENT_OBJECT,
    ARRAY_ELEMENT_SOFT_OBJECT,
    ARRAY_ELEMENT_STR,
    ARRAY_ELEMENT_STRUCT,
    ARRAY_PROPERTY,
    FLOAT_QUATERNION,
    FLOAT_VECTOR_3,
    OBJECT_REFERENCE,
    TEXT_ARGUMENT_INT,
    TEXT_ARGUMENT_TEXT,
    TEXT_PROPERTY,
    TEXT_VALUE_BASE,
    TEXT_VALUE_NONE,
    TEXT_VALUE_STRING_TABLE_ENTRY,
    TEXT_VALUE_TRANSFORM,
    TEXT_VALUE_WITH_ARGUMENTS,
)

map_keys = (
    (KeyTypeName.INT, 2_000_000_000),
    (KeyTypeName.INT64, 5_000_000_000_000_000_000),
    (KeyTypeName.NAME, "Root"),
    (KeyTypeName.STR, "Root"),
    (KeyTypeName.ENUM, "Enum::Value"),
    (KeyTypeName.OBJECT, OBJECT_REFERENCE),
    (KeyTypeName.STRUCT, (2_000_000_000, 2_000_000_000, 2_000_000_000)),
)

map_values = (
    (ValueTypeName.BOOL, True),
    (ValueTypeName.INT, 2_000_000_000),
    (ValueTypeName.INT64, 5_000_000_000_000_000_000),
    (ValueTypeName.FLOAT, 3.1434),
    (ValueTypeName.DOUBLE, 3.1434),
    (ValueTypeName.STR, "Root"),
    (ValueTypeName.OBJECT, OBJECT_REFERENCE),
    (
        ValueTypeName.TEXT,
        TextValueBase(flags=0, namespace="ns", key="key", value="value"),
    ),
    (
        ValueTypeName.STRUCT,
        PropertyList(items={"isRoot": BoolProperty(name="isRoot", value=True, index=0)}),
    ),
)


ITEMS = (
    TEXT_VALUE_BASE,
    TEXT_ARGUMENT_INT,
    TEXT_ARGUMENT_TEXT,
    TEXT_VALUE_WITH_ARGUMENTS,
    TEXT_VALUE_TRANSFORM,
    TEXT_VALUE_STRING_TABLE_ENTRY,
    TEXT_VALUE_NONE,
    TEXT_PROPERTY,
    ARRAY_ELEMENT_BYTE,
    ARRAY_ELEMENT_ENUM,
    ARRAY_ELEMENT_FLOAT,
    ARRAY_ELEMENT_INT,
    ARRAY_ELEMENT_INT64,
    ARRAY_ELEMENT_INTERFACE,
    ARRAY_ELEMENT_OBJECT,
    ARRAY_ELEMENT_SOFT_OBJECT,
    ARRAY_ELEMENT_STR,
    ARRAY_ELEMENT_STRUCT,
    ARRAY_ELEMENT_STRUCT,
    ARRAY_PROPERTY,
    # region map
    *[
        MapProperty(
            name="Root",
            index=0,
            key_type=key_en,
            value_type=value_en,
            mode=0,
            value=[(copy.copy(key_val), copy.copy(value_val))],
        )
        for key_en, key_val in map_keys
        for value_en, value_val in map_values
    ],
    MapProperty(
        name="Root",
        index=0,
        key_type=KeyTypeName.INT,
        value_type=ValueTypeName.BYTE,
        mode=0,
        value=[(2_000_000_000, 255)],
    ),
    MapProperty(
        name="Root",
        index=0,
        key_type=KeyTypeName.STR,
        value_type=ValueTypeName.BYTE,
        mode=0,
        value=[("Root", "Root")],
    ),
    # endregion
    # region set
    SetProperty(
        name="Root",
        set_type=SetType.U_INT_32,
        index=0,
        unk1=0,
        length=1,
        value=[3_000_000_000],
    ),
    SetProperty(
        name="Root",
        set_type=SetType.STRUCT,
        index=0,
        unk1=0,
        length=1,
        value=[(10_000_000_000_000_000_000, 10_000_000_000_000_000_000)],
    ),
    SetProperty(
        name="Root",
        set_type=SetType.OBJECT,
        index=0,
        unk1=0,
        length=1,
        value=[OBJECT_REFERENCE],
    ),
    # endregion
    # region simple_props
    BoolProperty(name="Root", index=0, value=True),
    ByteProperty(name="Root", index=0, type="None", value=b64_bytes(b"\x00\xff")),
    DoubleProperty(name="Root", index=0, value=3.1434),
    FloatProperty(name="Root", index=0, value=3.1434),
    EnumProperty(name="Root", index=0, type="Enum", value="Value"),
    Int8Property(name="Root", index=0, value=-125),
    Int64Property(name="Root", index=0, value=5_000_000_000_000_000_000),
    IntProperty(name="Root", index=0, value=2_000_000_000),
    NameProperty(name="Root", index=0, value="value"),
    ObjectProperty(name="Root", index=0, value=OBJECT_REFERENCE),
    SoftObjectProperty(name="Root", index=0, value=(OBJECT_REFERENCE, 1000)),
    StrProperty(name="Root", index=0, value="value"),
    UInt32Property(name="Root", index=0, value=3_000_000_000),
    # endregion
    # region struct
    StructProperty(
        name="Root",
        index=0,
        type=StructTypeName.DATE_TIME,
        unk1=b64_bytes(b"\x00" * 17),
        value=DateTime(value=int(time.time())),
    ),
    # endregion
    # region typed_data
    Box(
        min_x=3.1434,
        min_y=3.1434,
        min_z=3.1434,
        max_x=3.1434,
        max_y=3.1434,
        max_z=3.1434,
        is_valid=True,
    ),
    FluidBox(value=3.1434),
    InventoryItem(
        name="Root",
        unknown=0,
    ),
    LinearColor(r=0.5, g=0.5, b=0.5, a=0.5),
    DoubleQuaternion(x=3.1434, y=3.1434, z=3.1434, w=1),
    FLOAT_QUATERNION,
    RailroadTrackPosition(
        object_reference=OBJECT_REFERENCE,
        offset=3.1434,
        forward=3.1434,
    ),
    FLOAT_VECTOR_3,
    DoubleVector3(x=3.1434, y=3.1434, z=3.1434),
    DateTime(value=int(time.time())),
    ClientIdentityInfoIdentity(
        variant=ClientIdentityInfoIdentityVariant.STEAM,
        payload=b64_bytes(b"\x00\xff"),
    ),
    ClientIdentityInfo(
        uuid=str(uuid.uuid4()),
        identities=[
            ClientIdentityInfoIdentity(
                variant=ClientIdentityInfoIdentityVariant.STEAM,
                payload=b64_bytes(b"\x00\xff"),
            ),
        ],
    ),
    SpawnData(
        name="Root",
        type="ObjectProperty",
        level_path=OBJECT_REFERENCE,
        properties=PropertyList(items={"isRoot": BoolProperty(name="isRoot", value=True, index=0)}),
    ),
    # endregion
)


@pytest.mark.parametrize(
    ("item_cls", "item"),
    [(item.__class__, item) for item in ITEMS],
    ids=(f"serde {get_struct_name(item.__class__)}" for item in ITEMS),
)
def test_properties_serde[T](item_cls: type[T], item: T):
    ser = Serializer()
    ser.add(typing.cast("Serializable", item))
    calculated = Deserializer(ser.content).get(typing.cast("Deserializable", item_cls))  # type: ignore
    assert calculated == item
