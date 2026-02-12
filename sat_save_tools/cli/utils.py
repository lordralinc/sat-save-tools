import argparse
import pathlib

import rich.console
import rich.panel
from argcomplete.completers import BaseCompleter, FilesCompleter

__all__ = ("AnswerManager", "set_completer")

console = rich.console.Console()


class AnswerManager:
    @classmethod
    def success(cls, title: str, message: rich.console.RenderableType) -> None:
        console.print(
            rich.panel.Panel(
                message,
                title=f"[bold white]{title}[/]",
                border_style="green",
                expand=False,
            ),
        )

    @classmethod
    def error(cls, title: str, message: rich.console.RenderableType) -> None:
        console.print(
            rich.panel.Panel(
                message,
                title=f"[bold white]{title}[/]",
                border_style="red",
                expand=False,
            ),
        )


def set_completer(action: argparse.Action, completer: BaseCompleter) -> None:
    action.completer = completer  # type: ignore[attr-defined]


def add_input_file_action(parser: argparse.ArgumentParser) -> argparse.Action:
    action = parser.add_argument("save_path", type=pathlib.Path, help="Path to the input save file")
    set_completer(action, FilesCompleter([".sav", ".json"], directories=False))
    return action


def add_output_file_action(parser: argparse.ArgumentParser) -> argparse.Action:
    action = parser.add_argument(
        "--output",
        "-o",
        type=pathlib.Path,
        help="Path to the output save file",
    )
    set_completer(action, FilesCompleter([".sav", ".json"], directories=False))
    return action
