import pathlib
from argparse import ArgumentParser, _SubParsersAction

import rich
import rich.panel

from sat_save_tools.satisfactory_save import SatisfactorySaveFile

console = rich.console.Console()


def set_session_name_command(
    filename: pathlib.Path,
    session_name: str,
    output: pathlib.Path | None = None,
):
    output = output or filename
    file = SatisfactorySaveFile.load_from_json(filename)

    file.header.session_name = session_name

    file.save_to_json(output)

    console.print(
        rich.panel.Panel(
            f"Saved to {output}",
            title="[bold white]Set session name result[/]",
            border_style="green",
            expand=False,
        ),
    )


def setup(
    subparsers: _SubParsersAction[ArgumentParser],
):
    parser = subparsers.add_parser("set-session-name", help="Set session name")
    parser.add_argument("filename", type=pathlib.Path, help="Path to the JSON file")
    parser.add_argument("session-name", type=str, help="Session name")
    parser.add_argument(
        "--output",
        "-o",
        type=pathlib.Path,
        required=False,
        help="Path to output JSON file; if not set, saved in {filename}.json",
    )
    parser.set_defaults(func=set_session_name_command)
