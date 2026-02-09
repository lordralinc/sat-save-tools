import typing

from . import inventory, show

if typing.TYPE_CHECKING:
    import argparse

__all__ = ("setup",)


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    players_parser = subparsers.add_parser("players", help="Actions with players")
    players_subparsers = players_parser.add_subparsers(required=True)

    show.setup(players_subparsers)
    inventory.setup(players_subparsers)
