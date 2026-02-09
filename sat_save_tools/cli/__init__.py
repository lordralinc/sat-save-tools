import typing

from . import (
    export_consts_data,
    find_free_staff,
    generate_markdown,
    html,
    info,
    json,
    players,
    set_session_name,
    world_map,
)

if typing.TYPE_CHECKING:
    import argparse


__all__ = (
    "generate_markdown",
    "setup",
)


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    info.setup(subparsers)
    json.setup(subparsers)
    export_consts_data.setup(subparsers)
    set_session_name.setup(subparsers)
    html.setup(subparsers)
    players.setup(subparsers)
    world_map.setup(subparsers)
    find_free_staff.setup(subparsers)
