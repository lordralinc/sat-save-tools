import pathlib
import typing

import rich
import rich.table

from sat_save_tools import (
    ArrayProperty,
    DoubleProperty,
    PropertyList,
    SatisfactorySaveFile,
)
from sat_save_tools.cli.answers import AnswerManager
from sat_save_tools.models.properties.base import BaseProperty
from sat_save_tools.models.properties.typed_data import UUIDGUID

if typing.TYPE_CHECKING:
    import argparse

__all__ = ("setup",)


def show_map_markers(
    filename: pathlib.Path,
):
    try:
        file = SatisfactorySaveFile.load_from_file(filename)
        map_manager = file.body.persistent_level.objects.get("Persistent_Level:PersistentLevel.MapManager")
        if map_manager is None:
            AnswerManager.error("show map markers", "Map manager not found in the save file")
            return
        markers = map_manager.properties.get_value_or_none("mMapMarkers", result=ArrayProperty)
    except Exception:  # noqa: BLE001
        markers = ArrayProperty.model_validate_json(filename.read_text())
    if markers is None:
        AnswerManager.error("show map markers", "No map markers found in the save file")
        return
    table = rich.table.Table()

    table.add_column("ID", style="bold cyan", no_wrap=True)
    table.add_column("Location", style="green", no_wrap=True)
    table.add_column("Category", style="magenta", no_wrap=True)
    table.add_column("Name", style="bold white", no_wrap=True)
    table.add_column("Marker type", style="yellow", no_wrap=True)
    table.add_column("Icon ID", style="blue", no_wrap=True)
    table.add_column("Compass view distance", style="bright_black", no_wrap=True)
    table.add_column("Account ID", style="cyan", no_wrap=True)

    for marker in markers.value.elements:
        marker = typing.cast("PropertyList", marker)
        marker_id = marker.get_value_or_none("markerGuid", result=BaseProperty[UUIDGUID])
        location = marker.get_value_or_none("Location", result=BaseProperty[PropertyList])
        category = marker.get_value_or_none("CategoryName", result=BaseProperty[str])
        name = marker.get_value_or_none("Name", result=BaseProperty[str])
        marker_type = marker.get_value_or_none("MapMarkerType", result=BaseProperty[str])
        icon_id = marker.get_value_or_none("IconID", result=BaseProperty[str])
        compass_view_distance = marker.get_value_or_none("compassViewDistance", result=BaseProperty[str])
        account_id = marker.get_value_or_none("MarkerPlacedByAccountID", result=BaseProperty[str])

        if location is not None:
            loc_x = location.value.get_value("X", result=DoubleProperty).value
            loc_y = location.value.get_value("Y", result=DoubleProperty).value
            loc_z = location.value.get_value("Z", result=DoubleProperty).value
            loc_str = f"X = {loc_x:.2f}, Y = {loc_y:.2f}, Z = {loc_z:.2f}"
        else:
            loc_str = "N/A"

        table.add_row(
            str(marker_id.value) if marker_id else "N/A",
            loc_str,
            category.value if category else "N/A",
            name.value if name else "N/A",
            (marker_type.value.removeprefix("ERepresentationType::") if marker_type else "N/A"),
            str(icon_id.value) if icon_id else "N/A",
            (
                str(compass_view_distance.value.removeprefix("ECompassViewDistance::"))
                if compass_view_distance
                else "N/A"
            ),
            str(account_id.value) if account_id else "N/A",
        )
    AnswerManager.success(f"show map markers in {filename}", table)


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    parser = subparsers.add_parser("show", help="Show map markers")
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        help="Path to the save file or JSON file to show map markers from",
    )
    parser.set_defaults(func=show_map_markers)
