import typing

from . import markers

if typing.TYPE_CHECKING:
    import argparse

__all__ = ("setup",)


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    parser = subparsers.add_parser("map", help="Actions with map")
    map_subparsers = parser.add_subparsers(required=True)

    markers.setup(map_subparsers)
