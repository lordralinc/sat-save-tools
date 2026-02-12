import typing

from . import export

if typing.TYPE_CHECKING:
    import argparse

__all__ = ("setup",)


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    somersloops_parser = subparsers.add_parser("somersloops", help="Actions with somersloops")
    somersloops_subparsers = somersloops_parser.add_subparsers(required=True)

    export.setup(somersloops_subparsers)
