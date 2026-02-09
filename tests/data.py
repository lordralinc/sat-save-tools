# region text
from sat_save_tools import (
    ArrayElementEnum,
    ArrayElementFloat,
    ArrayElementInt,
    ArrayElementInt64,
    ArrayElementInterface,
    ArrayElementObject,
    ArrayElementSoftObject,
    ArrayElementStr,
    ArrayElementStruct,
    ArrayProperty,
    DateTime,
    ObjectReference,
    StructTypeName,
    TextArgumentInt,
    TextArgumentText,
    TextProperty,
    TextValueBase,
    TextValueNone,
    TextValueStringTableEntry,
    TextValueTransform,
    TextValueWithArguments,
)
from sat_save_tools.models.object_header import FloatVector3
from sat_save_tools.models.properties import PropertyList
from sat_save_tools.models.properties.array import ArrayElementByte, b64_bytes
from sat_save_tools.models.properties.typed_data import FloatQuaternion

OBJECT_REFERENCE = ObjectReference(
    level_name="ObjectReference.level_name",
    path_name="ObjectReference.path_name",
)
TEXT_VALUE_BASE = TextValueBase(
    flags=0,
    namespace="TextValueBase.namespace",
    key="TextValueBase.key",
    value="TextValueBase.value",
)
TEXT_ARGUMENT_INT = TextArgumentInt(name="TextArgumentInt.name", value=2_000_000_000, unknown=0)
TEXT_ARGUMENT_TEXT = TextArgumentText(name="TextArgumentText.name", value=TEXT_VALUE_BASE)
TEXT_VALUE_WITH_ARGUMENTS = TextValueWithArguments(
    source_format=TEXT_VALUE_BASE,
    flags=0,
    arguments=[
        TEXT_ARGUMENT_INT,
        TEXT_ARGUMENT_TEXT,
    ],
)
TEXT_VALUE_TRANSFORM = TextValueTransform(
    source_text=TEXT_VALUE_BASE,
    transform_type=0,
    flags=0,
)
TEXT_VALUE_STRING_TABLE_ENTRY = TextValueStringTableEntry(
    table_id="TextValueStringTableEntry.table_id",
    table_key="TextValueStringTableEntry.table_key",
    flags=0,
)
TEXT_VALUE_NONE = TextValueNone(
    has_culture_invariant_string=True,
    value="TextValueNone.value",
    flags=0,
)
TEXT_PROPERTY = TextProperty(name="TextProperty.name", index=0, value=TEXT_VALUE_BASE)
# endregion


# region array
ARRAY_ELEMENT_BYTE = ArrayElementByte(length=2, elements=b64_bytes(b"\x00\xff"))
ARRAY_ELEMENT_ENUM = ArrayElementEnum(length=1, elements=["Test::Value"])
ARRAY_ELEMENT_FLOAT = ArrayElementFloat(length=1, elements=[3.1434])
ARRAY_ELEMENT_INT = ArrayElementInt(length=1, elements=[2_000_000_000])
ARRAY_ELEMENT_INT64 = ArrayElementInt64(length=1, elements=[5_000_000_000_000_000_000])
ARRAY_ELEMENT_INTERFACE = ArrayElementInterface(length=1, elements=[OBJECT_REFERENCE])
ARRAY_ELEMENT_OBJECT = ArrayElementObject(length=1, elements=[OBJECT_REFERENCE])
ARRAY_ELEMENT_SOFT_OBJECT = ArrayElementSoftObject(length=1, elements=[(OBJECT_REFERENCE, 1)])
ARRAY_ELEMENT_STR = ArrayElementStr(length=1, elements=["Test"])
ARRAY_ELEMENT_STRUCT = ArrayElementStruct(
    name="ArrayElementStruct.name",
    type_name="ArrayElementStruct.type_name",
    length=1,
    payload_size=8,
    element_type=StructTypeName.DATE_TIME,
    uuid=b64_bytes(b"\x00" * 17),
    elements=[DateTime(value=0)],
)
ARRAY_PROPERTY = ArrayProperty(name="ArrayProperty.name", index=0, value=ARRAY_ELEMENT_BYTE)
# endregion


FLOAT_QUATERNION = FloatQuaternion(x=3.1434, y=3.1434, z=3.1434, w=1)
FLOAT_VECTOR_3 = FloatVector3(x=3.1434, y=3.1434, z=3.1434)


PROPERTY_LIST = PropertyList(items={TEXT_PROPERTY.name: TEXT_PROPERTY, ARRAY_PROPERTY.name: ARRAY_PROPERTY})
