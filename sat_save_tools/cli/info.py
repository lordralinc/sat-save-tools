import pathlib
from argparse import ArgumentParser, _SubParsersAction

import rich
from rich.table import Table

from sat_save_tools import Deserializer, SaveFileHeader
from sat_save_tools.cli.answers import AnswerManager
from sat_save_tools.utils import b64_bytes

console = rich.console.Console()


def info_command(filename: pathlib.Path, json: bool = False, plain: bool = False) -> None:
    if not filename.exists():
        AnswerManager.error("Info", f"File {filename} does not exist")
        return

    file = filename.read_bytes()
    des = Deserializer(file)

    file_info = des.get(SaveFileHeader)
    if json:
        (print if plain else console.print)(file_info.model_dump_json(indent=2 if not plain else None))
        return

    table = Table(title=f"Save file info: {filename.name}", show_lines=True)

    table.add_column("Field", style="bold cyan")
    table.add_column("Value", style="magenta", no_wrap=False, overflow="fold")
    table.add_column("Description", style="green")

    table.add_row("Header Type", str(file_info.header_version), "Save header version")
    table.add_row("Save Version", str(file_info.save_version), "Save version")
    table.add_row("Build Version", str(file_info.build_version), "Build version")
    table.add_row("Save Name", file_info.save_name, "Save name")
    table.add_row("Map Name", file_info.map_name, "Map name")
    table.add_row("Map Options", file_info.map_options, "Map options")
    table.add_row("Session Name", file_info.session_name, "Session name")
    table.add_row(
        "Play Duration",
        f"{file_info.play_timedelta} | {file_info.play_duration}",
        "Play duration",
    )
    table.add_row(
        "Save Datetime",
        f"{file_info.save_datetime} | {file_info.save_ticks}",
        "Save date and time",
    )
    table.add_row("Flags", str(file_info.flags), "Flags")
    table.add_row(
        "Editor Object Version",
        str(file_info.editor_object_version),
        "Editor object version",
    )
    table.add_row("Mod Metadata", file_info.mod_metadata, "Mod metadata")
    table.add_row("Mod Flags", str(file_info.mod_flags), "Mod flags")
    table.add_row("Save ID", file_info.save_id, "Save ID")
    table.add_row(
        "Is Partitioned World",
        str(file_info.is_partitioned_world),
        "Is partitioned world",
    )
    table.add_row(
        "Creative Mode Enabled",
        str(file_info.creative_mode_enabled),
        "Is creative mode enabled",
    )
    table.add_row("Checksum", str(b64_bytes(file_info.checksum)), "Checksum")
    table.add_row("Is Cheat", str(file_info.is_cheat), "Is cheat enabled")
    console.print(table, soft_wrap=True)


def setup(subparsers: _SubParsersAction[ArgumentParser]):
    parser = subparsers.add_parser("info", help="Show save info")
    parser.add_argument("filename", type=pathlib.Path, help="Path to the save file")
    parser.add_argument("--json", "-j", action="store_true", help="Show as JSON")
    parser.add_argument(
        "--plain",
        "-p",
        action="store_true",
        help="Disable indent and colors for JSON output",
    )
    parser.set_defaults(func=info_command)
