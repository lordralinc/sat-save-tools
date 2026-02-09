import pathlib
import typing
import uuid

from sat_save_tools import (
    BaseArrayElement,
    BaseProperty,
    PropertyList,
    SatisfactorySaveFile,
)
from sat_save_tools.cli.answers import AnswerManager
from sat_save_tools.models.properties.typed_data import UUIDGUID

if typing.TYPE_CHECKING:
    import argparse

__all__ = ("setup",)


def remove_map_marker(filename: pathlib.Path, output: pathlib.Path, marker_ids: list[uuid.UUID]):
    file = SatisfactorySaveFile.load_from_file(filename)
    map_manager = file.body.persistent_level.objects.get("Persistent_Level:PersistentLevel.MapManager")
    if map_manager is None:
        AnswerManager.error("remove map markers", "Map manager not found in the save file")
        return
    markers = map_manager.properties.get_value_or_none(
        "mMapMarkers",
        result=BaseProperty[BaseArrayElement[list[PropertyList]]],
    )
    if markers is None:
        AnswerManager.error("remove map markers", "No map markers found in the save file")
        return

    typing.cast(
        "BaseArrayElement[list[PropertyList]]",
        file.body.persistent_level.objects["Persistent_Level:PersistentLevel.MapManager"]
        .properties.items["mMapMarkers"]
        .value,
    ).elements = [
        marker
        for marker in markers.value.elements
        if marker.get_value("markerGuid", result=BaseProperty[UUIDGUID]).value not in marker_ids
    ]
    file.save_to_file(output)
    AnswerManager.success(
        "remove map markers",
        f"Writed file to {output}",
    )


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    parser = subparsers.add_parser("remove", help="Remove map markers")
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        help="Path to the save file",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        help="Path to output",
    )
    parser.add_argument(
        "--id",
        "-i",
        action="append",
        dest="marker_ids",
        type=uuid.UUID,
        default=[],
        help="Marker IDs",
    )
    parser.set_defaults(func=remove_map_marker)
