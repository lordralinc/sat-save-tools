import json
import pathlib
import typing
from argparse import ArgumentParser, _SubParsersAction
from collections import defaultdict
from functools import reduce
from hashlib import md5

import pydantic
from argcomplete.completers import FilesCompleter

from sat_save_tools import HeaderType, KeyTypeName, SatisfactorySaveFile, SetType, ValueTypeName
from sat_save_tools.cli.utils import (  # noqa: F401
    AnswerManager,
    add_input_file_action,
    add_output_file_action,
    set_completer,
)
from sat_save_tools.models import LevelObjectType, PropertyTypeName
from sat_save_tools.models.properties import PropertyList
from sat_save_tools.models.properties.array import ObjectReference
from sat_save_tools.models.properties.enums import ArrayElementTypeName

__all__ = ("setup",)


class MD:
    @staticmethod
    def make_anchor(_id: str) -> str:
        return f'<a id="{_id}"></a>'

    @staticmethod
    def code(val: str) -> str:
        return "`" + val + "`"

    @staticmethod
    def code_block(val: str, lang: str = "json") -> str:
        return f"```{lang}\n" + val + "\n```"

    @staticmethod
    def make_id(name: str) -> str:
        return md5(name.encode("utf-8")).hexdigest()  # noqa: S324

    @staticmethod
    def spoiler(name: str, content: str) -> str:
        def _add_indent(v: str, i: int = 2) -> str:
            return "\n".join([" " * i + line for line in v.splitlines()])

        return f"""<details>
  <summary>{name}</summary>

{_add_indent(content, 2)}
</details>"""

    @staticmethod
    def make_table(
        headers: list[str],
        rows: list[list[str]],
        *,
        title: str | None = None,
        with_anchor: str | None = None,
    ) -> str:
        text = ""

        if title:
            text += f"## {title}"

        if with_anchor is not None:
            text += MD.make_anchor(with_anchor)

        if title or with_anchor:
            text += "\n\n"

        text += "| " + " | ".join(headers) + " |\n"
        text += "| " + " | ".join(" --- " for _ in headers) + " |\n"
        for row in rows:
            text += "| " + " | ".join(str(it) for it in row) + " |\n"
        return text + "\n\n"


type PropsTree = "dict[str, Property]"
TABLES_TO_RENDER: "dict[str, Property]" = {}


class Property(pydantic.BaseModel):
    category: str
    sub: "str | Property | list[Property] | PropsTree | None" = None
    original_type: str | None = None

    def __hash__(self) -> int:
        if isinstance(self.sub, list):
            sub_hash = hash(tuple(self.sub))
        elif isinstance(self.sub, dict):
            sub_hash = hash(tuple(self.sub.items()))
        else:
            sub_hash = hash(self.sub)

        return hash((self.category, sub_hash, self.original_type))

    def simplify(self) -> None:
        if self.sub is None or isinstance(self.sub, str):
            return
        if isinstance(self.sub, dict):
            return

        if isinstance(self.sub, Property):
            self.sub.simplify()
            return

        flat: list[Property] = []

        for item in self.sub:
            item.simplify()

            if self.category == "Union" and item.category == "Union":
                if isinstance(item.sub, list):
                    flat.extend(item.sub)
                elif isinstance(item.sub, Property):
                    flat.append(item.sub)
            else:
                flat.append(item)
        seen: set[Property] = set()
        result: list[Property] = []
        for p in flat:
            if p not in seen:
                seen.add(p)
                result.append(p)

        self.sub = result

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return NotImplemented
        return hash(self) == hash(value)

    def __build__(self) -> str:
        if self.sub is None:
            return MD.code(self.category)
        self.simplify()
        if isinstance(self.sub, dict):
            return f"{MD.code(self.category)}<[{MD.code(self.original_type)}](#{MD.make_id(self.original_type)})>"  # type: ignore
        if isinstance(self.sub, list):
            sub = ", ".join([sub_item.__build__() for sub_item in self.sub])
            return f"`{self.category}`<{sub}>"

        if isinstance(self.sub, str):
            sub = f"[{MD.code(self.sub)}](#{MD.make_id(self.sub)})" if self.sub.startswith("/") else MD.code(self.sub)
        else:
            sub = self.sub.__build__()

        return f"`{self.category}`<{sub}>"

    def __str__(self):
        return self.__build__()


class ObjectDescriptor(pydantic.BaseModel):
    type: HeaderType
    obj_type: str
    properties: PropsTree
    component: LevelObjectType

    @classmethod
    def from_object(cls, save_file: SatisfactorySaveFile, obj: LevelObjectType) -> typing.Self:
        return cls(
            type=obj.header.type,
            obj_type=obj.header.type_path,
            properties=cls.tree(save_file, obj.properties),
            component=obj,
        )

    @classmethod
    def merge(cls, a: typing.Self, b: typing.Self) -> typing.Self:
        if a.type != b.type:
            raise ValueError(f"type mismatch: {a.type!r} != {b.type!r}")
        if a.obj_type != b.obj_type:
            raise ValueError(f"obj_type mismatch: {a.obj_type!r} != {b.obj_type!r}")

        def merge_props(
            left: PropsTree,
            right: PropsTree,
            path: str = "",
        ) -> PropsTree:
            result: PropsTree = dict(left)

            for key, r_val in right.items():
                cur_path = f"{path}.{key}" if path else key

                if key not in result:
                    result[key] = r_val
                    continue

                l_val = result[key]

                if isinstance(l_val, dict) and isinstance(r_val, dict):
                    result[key] = merge_props(l_val, r_val, cur_path)  # type: ignore
                    continue

                if isinstance(l_val, Property) and isinstance(r_val, Property):
                    if l_val != r_val:
                        result[key] = Property(category="Union", sub=[l_val, r_val])
                    else:
                        result[key] = l_val
                    continue

                raise ValueError(f"type conflict at '{cur_path}': {type(l_val).__name__} vs {type(r_val).__name__}")

            return result

        return cls(
            type=a.type, obj_type=a.obj_type, properties=merge_props(a.properties, b.properties), component=a.component
        )

    @classmethod
    def make_type_from_rel_objects(
        cls,
        save_file: SatisfactorySaveFile,
        rel_objects: list[ObjectReference],
    ) -> Property:
        if len(rel_objects) == 0:
            return Property(category="ObjectReference")
        related_objects = [key.get_related_object_or_none(save_file) for key in rel_objects]
        related_types = list({it.header.type_path for it in related_objects if it is not None})
        if len(related_types) == 0:
            return Property(category="ObjectReference")
        if len(related_types) == 1:
            return Property(category="ObjectReference", sub=related_types[0])
        return Property(
            category="ObjectReference",
            sub=Property(category="Union", sub=[Property(category=t) for t in related_types]),
        )

    @classmethod
    def tree(cls, save_file: SatisfactorySaveFile, props: PropertyList) -> PropsTree:
        __simple_props__ = [
            PropertyTypeName.BOOL,
            PropertyTypeName.BYTE,
            PropertyTypeName.FLOAT,
            PropertyTypeName.DOUBLE,
            PropertyTypeName.INT,
            PropertyTypeName.INT8,
            PropertyTypeName.U_INT32,
            PropertyTypeName.INT64,
            PropertyTypeName.STR,
            PropertyTypeName.TEXT,
        ]

        tree: PropsTree = {}
        for key, value in props.items.items():
            if value.type_name in __simple_props__:
                tree[key] = Property(category=value.type_name.value.removesuffix("Property"))
            elif value.type_name == PropertyTypeName.ENUM:
                tree[key] = Property(category="Enum", sub=value.type)
            elif value.type_name == PropertyTypeName.OBJECT:
                tree[key] = Property(category="ObjectReference")

                related_object = value.value.get_related_object_or_none(save_file)
                if related_object:
                    tree[key] = Property(category="ObjectReference", sub=related_object.header.type_path)
            elif value.type_name == PropertyTypeName.SET:
                if value.set_type == SetType.OBJECT:
                    tree[key] = Property(
                        category="Set",
                        sub=cls.make_type_from_rel_objects(
                            save_file,
                            typing.cast("list[ObjectReference]", value.value),
                        ),
                    )
                if value.set_type == SetType.STRUCT:
                    tree[key] = Property(
                        category="Set",
                        sub=Property(category="Tuple", sub=[Property(category="U64"), Property(category="U64")]),
                    )
                if value.set_type == SetType.U_INT_32:
                    tree[key] = Property(
                        category="Set",
                        sub=Property(category="U32"),
                    )
            elif value.type_name == PropertyTypeName.MAP:
                match value.key_type:
                    case KeyTypeName.INT:
                        key_prop = Property(category="Key", sub="I32")
                    case KeyTypeName.INT64:
                        key_prop = Property(category="Key", sub="I64")
                    case KeyTypeName.NAME | KeyTypeName.STR | KeyTypeName.ENUM:
                        key_prop = Property(category="Key", sub="String")
                    case KeyTypeName.OBJECT:
                        key_prop = Property(
                            category="Key",
                            sub=cls.make_type_from_rel_objects(
                                save_file,
                                typing.cast("list[ObjectReference]", [it[0] for it in value.value]),
                            ),
                        )
                    case KeyTypeName.STRUCT:
                        key_prop = Property(
                            category="Key",
                            sub=Property(
                                category="Tuple",
                                sub=[
                                    Property(category="I32"),
                                    Property(category="I32"),
                                    Property(category="I32"),
                                ],
                            ),
                        )
                    case _:
                        typing.assert_never(value.key_type)
                match value.value_type:
                    case ValueTypeName.BYTE:
                        value_prop = Property(
                            category="Value",
                            sub=Property(
                                category="Union", sub=[Property(category="Byte"), Property(category="String")]
                            ),
                        )
                    case ValueTypeName.BOOL:
                        value_prop = Property(category="Value", sub=Property(category="U8Bool"))
                    case ValueTypeName.INT:
                        value_prop = Property(category="Value", sub=Property(category="I32"))
                    case ValueTypeName.INT64:
                        value_prop = Property(category="Value", sub=Property(category="I64"))
                    case ValueTypeName.FLOAT:
                        value_prop = Property(category="Value", sub=Property(category="Float"))
                    case ValueTypeName.DOUBLE:
                        value_prop = Property(category="Value", sub=Property(category="Double"))
                    case ValueTypeName.STR:
                        value_prop = Property(category="Value", sub=Property(category="String"))
                    case ValueTypeName.OBJECT:
                        value_prop = Property(
                            category="Value",
                            sub=cls.make_type_from_rel_objects(
                                save_file,
                                typing.cast(
                                    "list[ObjectReference]",
                                    [it[1] for it in value.value],
                                ),
                            ),
                        )
                    case ValueTypeName.TEXT:
                        value_prop = Property(category="Value", sub=Property(category="Text"))
                    case ValueTypeName.STRUCT:
                        prop_lists = [typing.cast("PropertyList", it[1]).items for it in value.value]
                        merged_prop_list = {}
                        for prop_list in prop_lists:
                            merged_prop_list.update(prop_list)
                        value_prop = Property(
                            category="Value",
                            sub=cls.tree(save_file, PropertyList(items=merged_prop_list)),
                            original_type=value.name + "Props",
                        )
                        TABLES_TO_RENDER[value.name + "Props"] = Property(
                            category="Value",
                            sub=cls.tree(save_file, PropertyList(items=merged_prop_list)),
                            original_type=value.name + "Props",
                        )
                    case _ as vt:
                        typing.assert_never(vt)
                tree[key] = Property(
                    category="Map",
                    sub=[key_prop, value_prop],
                )
            elif value.type_name == PropertyTypeName.SOFT_OBJECT:
                tree[key] = Property(
                    category="Tuple",
                    sub=[Property(category="ObjectReference"), Property(category="Int")],
                )
                related_object = value.value[0].get_related_object_or_none(save_file)
                if related_object:
                    tree[key] = Property(
                        category="Tuple",
                        sub=[
                            Property(category="ObjectReference", sub=related_object.header.type_path),
                            Property(category="Int"),
                        ],
                    )
            elif value.type_name == PropertyTypeName.ARRAY:
                if value.value.type == ArrayElementTypeName.STRUCT:
                    tree[key] = Property(
                        category="Array", sub=Property(category="Struct", sub=value.value.element_type.value)
                    )

                    elements = value.value.elements
                    if isinstance(elements, (bytes, bytearray, memoryview)):
                        continue
                    prop_lists = [el for el in elements if isinstance(el, PropertyList)]
                    merged_prop_list = PropertyList(items={})
                    for el in prop_lists:
                        merged_prop_list.items.update(el.items)
                    if not merged_prop_list.items:
                        continue
                    tree[key] = Property(
                        category="Array",
                        sub=Property(
                            category="Struct",
                            sub=cls.tree(save_file, merged_prop_list),
                            original_type=value.name + "Props",
                        ),
                    )
                    TABLES_TO_RENDER[value.name + "Props"] = Property(
                        category="Struct",
                        sub=cls.tree(save_file, merged_prop_list),
                        original_type=value.name + "Props",
                    )

                elif value.value.type in {ArrayElementTypeName.OBJECT, ArrayElementTypeName.INTERFACE}:
                    elements = value.value.elements
                    rel_objects = [el.get_related_object_or_none(save_file) for el in elements]  # type: ignore
                    types = list({obj.header.type_path for obj in rel_objects if obj is not None})
                    if len(types) < 1:
                        tree[key] = Property(
                            category="Array",
                            sub=Property(category="Struct", sub=Property(category="ObjectReference")),
                        )
                    else:
                        tree[key] = Property(
                            category="Array",
                            sub=Property(
                                category="Struct",
                                sub=Property(category="Union", sub=[Property(category=it) for it in types])
                                if len(types) > 1
                                else Property(category="Union", sub=types[0]),
                            ),
                        )
                else:
                    tree[key] = Property(category="Array", sub=value.value.type.value)

            elif value.type_name == PropertyTypeName.STRUCT:
                if isinstance(value.value, PropertyList):
                    tree[key] = Property(
                        category="Struct",
                        sub=cls.tree(save_file, value.value),
                        original_type=value.type.value,
                    )
                    TABLES_TO_RENDER[value.type.value] = Property(
                        category="Struct",
                        sub=cls.tree(save_file, value.value),
                        original_type=value.type.value,
                    )
                else:
                    tree[key] = Property(
                        category="Struct",
                        sub=value.type.value,
                        original_type=value.type.value,
                    )
            else:
                tree[key] = Property(category=value.type_name.value)
        return tree

    @classmethod
    def build_props(cls, tree: PropsTree, title: str, table_id: str | None = None) -> str:
        table = {"header": ["Name", "Type"], "rows": []}

        for key, value in tree.items():
            if isinstance(value.sub, dict):
                global_table_id = MD.make_id(value.original_type or "")
                table["rows"].append([key, f"[`{value.original_type}`](#{global_table_id})"])
            else:
                table["rows"].append([key, f"{value}"])

        return "\n\n" + MD.make_table(table["header"], table["rows"], title=title, with_anchor=table_id)


def command(save_path: pathlib.Path, output: pathlib.Path | None = None) -> None:
    if not save_path.exists():
        AnswerManager.error("SAV2JSON Result", f"File {save_path} does not exist")
        return

    output = output or save_path.with_suffix(".md")
    save_content = SatisfactorySaveFile.load_from_file(save_path)

    descriptors: dict[str, list[ObjectDescriptor]] = defaultdict(list)

    for level in save_content.body.full_levels:
        for obj in level.objects.values():
            descriptors[obj.header.type_path].append(ObjectDescriptor.from_object(save_content, obj))

    def make_tree(paths: list[str]):
        tree = lambda: defaultdict(tree)  # noqa: E731
        root = defaultdict(tree)

        for path in paths:
            parts = [f"`{p}`" for p in path.strip("/").split("/")]
            parts[-1] = f"[{parts[-1]}](#{MD.make_id(path)})"
            node = root
            for part in parts:
                node = node[part]

        return root

    def render_tree(d: dict, prefix: str = ""):
        text = ""
        for key, sub in sorted(d.items()):
            text += f"{prefix}- {key}\n"
            if sub:
                text += render_tree(sub, prefix + "  ")
        return text

    tree = make_tree(list(descriptors.keys()))
    toc = "# Content:\n\n" + render_tree(tree) + "\n"

    toc += "- [`Typed data`](#typed_data)\n"
    for key in TABLES_TO_RENDER:
        toc += f"  - [`{key}`](#{MD.make_id(key)})\n"

    text = f"""# Objects

[← Back](/notes/README.md)

A list of objects contained in the save file.

{toc}


"""
    for key, desc in {key: reduce(ObjectDescriptor.merge, value) for key, value in descriptors.items()}.items():
        text += f"""
## `{key}` {MD.make_anchor(MD.make_id(key))}

**Component type** `{desc.type.name}`


"""
        if desc.properties:
            text += ObjectDescriptor.build_props(desc.properties, title="Properties")

        text += f"[JSON Repr](/notes/objects_json/{key}.json)"
        json_output = pathlib.Path("notes", "objects_json", (key.removeprefix("/") + ".json"))
        json_output.parent.mkdir(exist_ok=True, parents=True)
        json_output.write_text(
            json.dumps(desc.component.model_dump(mode="json"), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        text += "\n\n"

    text += '\n\n# Typed Data <a id="typed_data"></a>\n\n'

    for table_key, table_data in TABLES_TO_RENDER.items():
        text += ObjectDescriptor.build_props(table_data.sub, title=table_key, table_id=MD.make_id(table_key)) + "\n\n"  # type: ignore

    output.write_text(text, encoding="utf-8")


def setup(
    subparsers: _SubParsersAction[ArgumentParser],
):
    parser = subparsers.add_parser("make-objects-tree", help="Build object tree")
    add_input_file_action(parser)
    set_completer(
        parser.add_argument("--output", "-o", type=pathlib.Path, help="Path to the output file"),
        FilesCompleter([".md"], directories=False),
    )
    parser.set_defaults(func=command)
