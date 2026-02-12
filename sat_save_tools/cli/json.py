import pathlib
from argparse import ArgumentParser, _SubParsersAction

import rich
import rich.panel

from sat_save_tools import SatisfactorySaveFile
from sat_save_tools.cli.utils import AnswerManager, add_input_file_action, add_output_file_action

__all__ = ("setup",)


def to_json_command(save_path: pathlib.Path, output: pathlib.Path | None = None) -> None:
    if not save_path.exists():
        AnswerManager.error("SAV2JSON Result", f"File {save_path} does not exist")
        return

    output = output or save_path.with_suffix(".json")

    save_content = SatisfactorySaveFile.load_from_file(save_path)
    save_content.save_to_json(output)
    AnswerManager.success(
        "SAV2JSON result",
        rich.panel.Panel(
            f"Saved to {output}",
            border_style="green",
            expand=False,
        ),
    )


def from_json_command(save_path: pathlib.Path, output: pathlib.Path | None = None) -> None:
    if not save_path.exists():
        AnswerManager.error("JSON2SAV Result", f"File {save_path} does not exist")
        return
    output = output or save_path.with_suffix(".sav")
    save_content = SatisfactorySaveFile.load_from_file(save_path)
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
    add_input_file_action(parser_to_json)
    add_output_file_action(parser_to_json)
    parser_to_json.set_defaults(func=to_json_command)

    parser_from_json = subparsers.add_parser("from-json", help="Save to sav")
    add_input_file_action(parser_from_json)
    add_output_file_action(parser_from_json)
    parser_from_json.set_defaults(func=from_json_command)
