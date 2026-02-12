import pathlib
from argparse import ArgumentParser, _SubParsersAction

import rich
import rich.panel

from sat_save_tools.cli.utils import add_input_file_action, add_output_file_action
from sat_save_tools.satisfactory_save import SatisfactorySaveFile

__all__ = ("setup",)

console = rich.console.Console()


def set_session_name_command(
    save_path: pathlib.Path,
    session_name: str,
    output: pathlib.Path | None = None,
):
    output = output or save_path
    file = SatisfactorySaveFile.load_from_file(save_path)

    file.header.session_name = session_name

    file.save_to_file(output)

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
    add_input_file_action(parser)
    parser.add_argument("session-name", type=str, help="Session name")
    add_output_file_action(parser)
    parser.set_defaults(func=set_session_name_command)
