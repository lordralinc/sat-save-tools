import json
import pathlib
import typing

from sat_save_tools import SatisfactorySaveFile
from sat_save_tools.cli.answers import AnswerManager

if typing.TYPE_CHECKING:
    import argparse

__all__ = ("setup",)


def export_map_markers(
    filename: pathlib.Path,
    output: pathlib.Path | None = None,
):
    output = output or filename.with_suffix(".map_markers.json")
    file = SatisfactorySaveFile.load_from_file(filename)
    map_manager = file.body.persistent_level.objects.get("Persistent_Level:PersistentLevel.MapManager")
    if map_manager is None:
        AnswerManager.error("export map markers", "Map manager not found in the save file")
        return
    markers = map_manager.properties.get_value_or_none("mMapMarkers")
    if markers is None:
        AnswerManager.error("export map markers", "No map markers found in the save file")
        return
    output.write_text(json.dumps(markers.model_dump(mode="json"), indent=2, ensure_ascii=False))
    AnswerManager.success(
        "export map markers",
        f"Exported map markers to {output}",
    )


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    parser = subparsers.add_parser("export", help="Export map markers")
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        help="Path to the save file to export map markers from",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        default=None,
        help="Path to output the exported map markers to (defaults: {filename}.map_markers.json)",
    )
    parser.set_defaults(func=export_map_markers)
