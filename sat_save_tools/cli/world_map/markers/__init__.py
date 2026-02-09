import typing

from . import add, export, remove, show

if typing.TYPE_CHECKING:
    import argparse

__all__ = ("setup",)


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    parser = subparsers.add_parser("markers", help="Actions with markers")
    markers_subparsers = parser.add_subparsers(required=True)

    show.setup(markers_subparsers)
    add.setup(markers_subparsers)
    export.setup(markers_subparsers)
    remove.setup(markers_subparsers)
