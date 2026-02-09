import pathlib
import typing

import rich
import rich.table

from sat_save_tools import SatisfactorySaveFile
from sat_save_tools.actions.players import get_player_list, get_player_nickname
from sat_save_tools.cli.answers import AnswerManager

if typing.TYPE_CHECKING:
    import argparse

    from sat_save_tools import BaseProperty, DoubleVector3

__all__ = ("setup",)


def show_player_list(filename: pathlib.Path) -> None:
    file = SatisfactorySaveFile.load_from_json(filename)
    players = get_player_list(file)

    table = rich.table.Table(show_lines=True)

    table.add_column("ID", style="bold cyan")
    table.add_column("Nickname", style="magenta")
    table.add_column("Position", style="green")

    for player in players:
        nickname = get_player_nickname(file, player) or "<unknown>"

        last_safe_character_location = typing.cast(
            "BaseProperty[DoubleVector3] | None",
            player.properties.get_value_or_none("mLastSafeCharacterLocation"),
        )
        pos = last_safe_character_location.value if last_safe_character_location is not None else player.header.position
        position = f"X: {pos.x:.2f}, Y: {pos.y:.2f}, Z: {pos.z:.2f}"
        table.add_row(player.header.instance_name, nickname, position)

    AnswerManager.success("player list", table)


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    list_parser = subparsers.add_parser("list", help="List all players in the save file")
    list_parser.add_argument("filename", type=pathlib.Path, help="Path to the JSON file")
    list_parser.set_defaults(func=show_player_list)
