import pathlib
from argparse import ArgumentParser, _SubParsersAction

import rich
import rich.panel

from sat_save_tools import SatisfactorySaveFile
from sat_save_tools.cli.answers import AnswerManager


def to_json_command(filename: pathlib.Path, output: pathlib.Path | None = None) -> None:
    if not filename.exists():
        AnswerManager.error("SAV2JSON Result", f"File {filename} does not exist")
        return

    output = output or filename.with_suffix(".json")

    save_content = SatisfactorySaveFile.load_from_file(filename)
    save_content.save_to_json(output)
    AnswerManager.success(
        "SAV2JSON result",
        rich.panel.Panel(
            f"Saved to {output}",
            border_style="green",
            expand=False,
        ),
    )


def from_json_command(filename: pathlib.Path, output: pathlib.Path | None = None) -> None:
    if not filename.exists():
        AnswerManager.error("JSON2SAV Result", f"File {filename} does not exist")
        return
    output = output or filename.with_suffix(".sav")
    save_content = SatisfactorySaveFile.load_from_file(filename)
    save_content.save_to_sav(output)
    AnswerManager.success(
        "JSON2SAV Result",
        rich.panel.Panel(
            f"Saved to {output}",
            border_style="green",
            expand=False,
        ),
    )


def setup(
    subparsers: _SubParsersAction[ArgumentParser],
):
    parser_to_json = subparsers.add_parser("to-json", help="Save to JSON")
    parser_to_json.add_argument("filename", type=pathlib.Path, help="Path to the save file")
    parser_to_json.add_argument(
        "--output",
        "-o",
        type=pathlib.Path,
        required=False,
        help="Path to output JSON file; if not set, saved in {input}.json",
    )
    parser_to_json.set_defaults(func=to_json_command)

    parser_from_json = subparsers.add_parser("from-json", help="Save to sav")
    parser_from_json.add_argument("filename", type=pathlib.Path, help="Path to the JSON file")
    parser_from_json.add_argument(
        "--output",
        "-o",
        type=pathlib.Path,
        required=False,
        help="Path to output sav file; if not set, saved in {input}.sav",
    )

    parser_from_json.set_defaults(func=from_json_command)
