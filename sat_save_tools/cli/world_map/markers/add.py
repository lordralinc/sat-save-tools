import argparse
import math
import pathlib
import typing
import uuid

from rich_argparse import ArgumentDefaultsRichHelpFormatter

from sat_save_tools import (
    ArrayElementStruct,
    ArrayProperty,
    BaseArrayElement,
    BaseProperty,
    ConstDataView,
    DoubleProperty,
    DoubleVector3,
    EnumProperty,
    IntProperty,
    LinearColor,
    PropertyList,
    SatisfactorySaveFile,
    SatisfactorySaveParserError,
    StrProperty,
    StructProperty,
    StructTypeName,
)
from sat_save_tools.cli.utils import AnswerManager
from sat_save_tools.const import MAP_MARKERS_LIMIT
from sat_save_tools.models.properties.typed_data import UUIDGUID
from sat_save_tools.utils import require

__all__ = ("setup",)


def add_markers(
    save_elements: list[PropertyList],
    src_elements: list[PropertyList],
    skip_len_check: bool = False,
) -> list[PropertyList]:
    result = save_elements + src_elements
    for i in range(len(result)):
        typing.cast("BaseProperty[UUIDGUID]", result[i].items["markerGuid"]).value = UUIDGUID(bytes=uuid.uuid4().bytes)
    if not skip_len_check and len(result) > MAP_MARKERS_LIMIT:
        raise SatisfactorySaveParserError("map_markers_limit", "Map markers limit reached")

    return result


def merge_markers(
    save_elements: list[PropertyList],
    src_elements: list[PropertyList],
    skip_len_check: bool = False,
) -> list[PropertyList]:
    def marker_guid(el: PropertyList) -> UUIDGUID:
        return el.get_value("markerGuid", result=BaseProperty[UUIDGUID]).value

    def location(el: PropertyList) -> PropertyList:
        return el.get_value("Location", result=PropertyList)

    def vec(loc: PropertyList) -> tuple[float, float, float]:
        def v(name: str) -> float:
            return loc.get_value(name, result=DoubleProperty).value

        return v("X"), v("Y"), v("Z")

    def same_location(a: PropertyList, b: PropertyList) -> bool:
        ax, ay, az = vec(location(a))
        bx, by, bz = vec(location(b))

        return (
            math.isclose(ax, bx, rel_tol=1e-9, abs_tol=1e-12)
            and math.isclose(ay, by, rel_tol=1e-9, abs_tol=1e-12)
            and math.isclose(az, bz, rel_tol=1e-9, abs_tol=1e-12)
        )

    result: list[PropertyList] = []
    used_src: set[int] = set()

    src_by_guid: dict[UUIDGUID, list[int]] = {}
    for i, el in enumerate(src_elements):
        src_by_guid.setdefault(marker_guid(el), []).append(i)

    for save_el in save_elements:
        guid = marker_guid(save_el)

        if guid in src_by_guid:
            used_src.update(src_by_guid[guid])
            result.append(save_el)
            continue

        matched = False
        for i, src_el in enumerate(src_elements):
            if i in used_src:
                continue
            if same_location(save_el, src_el):
                used_src.add(i)
                result.append(save_el)
                matched = True
                break

        if not matched:
            result.append(save_el)

    for i, src_el in enumerate(src_elements):
        if i not in used_src:
            result.append(src_el)
    if not skip_len_check and len(result) > MAP_MARKERS_LIMIT:
        raise SatisfactorySaveParserError("map_markers_limit", "Map markers limit reached")

    return result


def generate_marker(
    location: DoubleVector3,
    name: str,
    icon_id: int,
    account_id: str,
    guid: uuid.UUID | None = None,
    category_name: str = "",
    color: LinearColor | None = None,
    compass_view_distance: str = "ECompassViewDistance::CVD_Off",
) -> PropertyList:
    guid = guid or uuid.uuid4()
    color = color or LinearColor(r=1, g=1, b=1, a=1)

    return PropertyList(
        items={
            "markerGuid": StructProperty(
                name="markerGuid",
                value=UUIDGUID(bytes=guid.bytes),
                type=StructTypeName.GUID,
            ),
            "Location": StructProperty(
                name="Location",
                type=StructTypeName.VECTOR_NET_QUANTIZE,
                value=PropertyList(
                    items={
                        "X": DoubleProperty(
                            name="X",
                            value=location.x,
                        ),
                        "Y": DoubleProperty(
                            name="Y",
                            value=location.y,
                        ),
                        "Z": DoubleProperty(
                            name="Z",
                            value=location.z,
                        ),
                    },
                ),
            ),
            "Name": StrProperty(name="Name", value=name),
            "CategoryName": StrProperty(name="CategoryName", value=category_name),
            "MapMarkerType": EnumProperty(
                name="MapMarkerType",
                value="ERepresentationType::RT_Stamp",
                type="ERepresentationType",
            ),
            "IconID": IntProperty(name="IconID", value=icon_id),
            "Color": StructProperty(
                name="Color",
                type=StructTypeName.LINEAR_COLOR,
                ink1="AAAAAAAAAAAAAAAAAAAAAAA=",  # type: ignore
                value=color,
            ),
            "Scale": DoubleProperty(name="Scale", value=1.0),
            "CompassViewDistance": EnumProperty(
                name="CompassViewDistance",
                value=compass_view_distance,
                type="ECompassViewDistance",
            ),
            "MarkerPlacedByAccountID": StrProperty(
                name="MarkerPlacedByAccountID",
                value=require(account_id),
            ),
        },
    )


def add_map_markers(
    filename: pathlib.Path,
    output: pathlib.Path,
    recreate_ids: bool = False,
    account_id: str | None = None,
    src: pathlib.Path | None = None,
    mode: typing.Literal["add", "replace", "merge"] | None = None,
    ms: bool = False,
    ms_name: str = "Mercer Sphere",
    ms_compass_view_distance: str = "ECompassViewDistance::CVD_Off",
    ms_icon_id: int = 334,
    somersloops: bool = False,
    somersloops_name: str = "Somersloop",
    somersloops_compass_view_distance: str = "ECompassViewDistance::CVD_Off",
    somersloops_icon_id: int = 329,
    hd: bool = False,
    hd_name: str = "Hard drive",
    hd_compass_view_distance: str = "ECompassViewDistance::CVD_Off",
    hd_icon_id: int = 652,
) -> None:
    save = SatisfactorySaveFile.load_from_file(filename)
    data_view = ConstDataView()
    map_manager = save.body.persistent_level.objects.get("Persistent_Level:PersistentLevel.MapManager")
    if map_manager is None:
        AnswerManager.error("show map markers", "Map manager not found in the save file")
        return
    markers = map_manager.properties.get_value_or_none("mMapMarkers", result=ArrayProperty) or ArrayProperty(
        name="mMapMarkers",
        value=ArrayElementStruct(
            name="mMapMarkers",
            length=0,
            type_name="StructProperty",
            payload_size=0,
            element_type=StructTypeName.MAP_MARKER,
            uuid="AAAAAAAAAAAAAAAAAAAAAAA=",  # type: ignore
            elements=[],
        ),
        index=0,
    )
    if src:
        src_markers = ArrayProperty.model_validate_json(src.read_text())
        if mode == "add":
            typing.cast("BaseArrayElement[list[PropertyList]]", markers.value).elements = add_markers(
                typing.cast("list[PropertyList]", markers.value.elements),
                typing.cast("list[PropertyList]", src_markers.value.elements),
            )
        elif mode == "replace":
            typing.cast("BaseArrayElement[list[PropertyList]]", markers.value).elements = typing.cast(
                "list[PropertyList]",
                src_markers.value.elements,
            )
        else:
            typing.cast("BaseArrayElement[list[PropertyList]]", markers.value).elements = merge_markers(
                typing.cast("list[PropertyList]", markers.value.elements),
                typing.cast("list[PropertyList]", src_markers.value.elements),
            )

    if ms:
        spheres = data_view.mercer_spheres
        for level in [*save.body.levels, save.body.persistent_level]:
            for collectable in [
                *(level.collectables or []),
                *(level.second_collectables or []),
            ]:
                if collectable.path_name in spheres:
                    del spheres[collectable.path_name]

        new_markers = [
            generate_marker(
                location=sphere.position,
                name=ms_name,
                icon_id=ms_icon_id,
                account_id=require(account_id),
                compass_view_distance=ms_compass_view_distance,
            )
            for sphere in spheres.values()
        ]
        typing.cast("BaseArrayElement[list[PropertyList]]", markers.value).elements = merge_markers(
            typing.cast("list[PropertyList]", markers.value.elements),
            typing.cast("list[PropertyList]", new_markers),
        )

    if somersloops:
        somersloops_data = data_view.somersloop
        for level in [*save.body.levels, save.body.persistent_level]:
            for collectable in [
                *(level.collectables or []),
                *(level.second_collectables or []),
            ]:
                if collectable.path_name in somersloops_data:
                    del somersloops_data[collectable.path_name]
        new_markers = [
            generate_marker(
                location=somersloop.position,
                name=somersloops_name,
                icon_id=somersloops_icon_id,
                account_id=require(account_id),
                compass_view_distance=somersloops_compass_view_distance,
            )
            for somersloop in somersloops_data.values()
        ]

    if hd:
        crash_sites = data_view.crash_sites
        for level in [*save.body.levels, save.body.persistent_level]:
            for collectable in [
                *(level.collectables or []),
                *(level.second_collectables or []),
            ]:
                if collectable.path_name in crash_sites:
                    del crash_sites[collectable.path_name]
        new_markers = [
            generate_marker(
                location=crash_site.position,
                name=hd_name,
                icon_id=hd_icon_id,
                account_id=require(account_id),
                compass_view_distance=hd_compass_view_distance,
            )
            for crash_site in crash_sites.values()
        ]

    if recreate_ids:
        for element in typing.cast("list[PropertyList]", markers.value.elements):
            typing.cast("BaseProperty[UUIDGUID]", element.items["markerGuid"]).value = UUIDGUID(
                bytes=uuid.uuid4().bytes,
            )
    if account_id:
        for element in typing.cast("list[PropertyList]", markers.value.elements):
            element.items["MarkerPlacedByAccountID"] = StrProperty(
                name="MarkerPlacedByAccountID",
                value=account_id,
                index=0,
            )
    save.body.persistent_level.objects["Persistent_Level:PersistentLevel.MapManager"].properties.items[
        "mMapMarkers"
    ] = markers
    save.save_to_file(output)
    AnswerManager.success("add map markers", f"Map markers added and saved to {output}")


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
    parser = subparsers.add_parser(
        "add",
        help="Add map markers",
        formatter_class=ArgumentDefaultsRichHelpFormatter,
    )
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        help="Save file path",
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        type=pathlib.Path,
        help="Output save file path",
    )
    parser.add_argument(
        "--recreate-ids",
        action="store_true",
        help="Recreate marker IDs",
    )

    parser.add_argument(
        "--account-id",
        type=str,
        help="Account ID (required for account-bound markers)",
    )
    parser.add_argument(
        "--skip-len-check",
        action="store_true",
        help="Disable the marker limit check",
    )

    file_group = parser.add_argument_group("File import")
    file_group.add_argument(
        "--src",
        type=pathlib.Path,
        help="Source JSON file with markers",
    )
    file_group.add_argument(
        "--mode",
        choices=("add", "replace", "merge"),
        help="Import mode",
    )

    mc_group = parser.add_argument_group("Mercer spheres")
    mc_group.add_argument("--ms", action="store_true", help="Add Mercer spheres")
    mc_group.add_argument("--ms-name", default="Mercer Sphere", help="Name of the Mercer sphere markers")
    mc_group.add_argument(
        "--ms-compass-view-distance",
        default="ECompassViewDistance::CVD_Off",
        help="Compass view distance for Mercer spheres",
    )
    mc_group.add_argument(
        "--ms-icon-id",
        type=int,
        default=334,
        help="Icon ID for Mercer spheres. See icon_ids.json.",
    )

    somers_group = parser.add_argument_group("Somersloops")
    somers_group.add_argument(
        "--somersloops",
        action="store_true",
        help="Add Somersloops",
    )
    somers_group.add_argument(
        "--somersloops-name",
        default="Somersloop",
        help="Name of the Somersloop markers",
    )
    somers_group.add_argument(
        "--somersloops-compass-view-distance",
        default="ECompassViewDistance::CVD_Off",
        help="Compass view distance for Somersloops",
    )
    somers_group.add_argument(
        "--somersloops-icon-id",
        type=int,
        default=329,
        help="Icon ID for Somersloops. See icon_ids.json.",
    )

    hd_group = parser.add_argument_group("Hard drives")
    hd_group.add_argument("--hard-drives", "-hd", action="store_true", help="Add Hard Drives")
    hd_group.add_argument("--hd-name", default="Hard drive", help="Name of the Hard Drive markers")
    hd_group.add_argument(
        "--hd-compass-view-distance",
        default="ECompassViewDistance::CVD_Off",
        help="Compass view distance for Hard Drives",
    )
    hd_group.add_argument(
        "--hd-icon-id",
        type=int,
        default=652,
        help="Icon ID for Hard Drives. See icon_ids.json.",
    )

    def _validate(args: argparse.Namespace) -> None:
        if args.mode == "add" and not args.recreate_ids:
            parser.error("--mode add requires --recreate-ids")

        if (args.src or args.mode) and not (args.src and args.mode):
            parser.error("--src and --mode must be used together")

        if (args.ms or args.somersloops or args.hd) and not args.account_id:
            parser.error("--account-id is required for ms3 / somersloops / hd")

    parser.set_defaults(_validate=_validate)
    parser.set_defaults(func=add_map_markers)
