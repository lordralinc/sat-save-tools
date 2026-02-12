#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse
import logging
import pathlib
import sys

import argcomplete
from rich.logging import RichHandler
from rich_argparse import RichHelpFormatter

from . import cli
from .const import TRACE_BIN_LOG_LEVEL
from .data import ConstDataView
from .logger import ContextFilter

RICH_FORMAT = "%(name)s %(context)s - %(message)s"

parser = argparse.ArgumentParser(
    prog="sst",
    description="Satisfactory save tools CLI",
    formatter_class=(RichHelpFormatter if "gen-cli-docs" not in sys.argv else argparse.HelpFormatter),
)
parser.add_argument("--log-level", type=str, default="INFO", help="Set log level")
parser.add_argument("--disable-logging", action="store_true", help="Disable logging")
parser.add_argument(
    "--data-folder",
    type=pathlib.Path,
    required=False,
    help="Path to static JSON data",
)

subparsers = parser.add_subparsers(required=True)
cli.setup(subparsers)
cli.generate_markdown.setup(subparsers, parser)


argcomplete.autocomplete(parser)


def main():
    args = parser.parse_args()

    if args.func is None:
        parser.print_help()
        raise SystemExit(1)

    kwargs = vars(args)
    func = kwargs.pop("func")

    if hasattr(args, "_validate"):
        _validate = kwargs.pop("_validate")
        _validate(args)

    if kwargs.pop("disable_logging"):
        logging.disable(logging.CRITICAL)
    else:
        log_level = kwargs.pop("log_level")
        context_filter = ContextFilter()

        console_handler = RichHandler(
            rich_tracebacks=True,
            tracebacks_show_locals=True,
            keywords=["TRACE_BIN"],
        )
        console_handler.addFilter(context_filter)
        console_handler.setFormatter(logging.Formatter(RICH_FORMAT, datefmt="[%X]"))

        if log_level == "TRACE_BIN":
            log_level = TRACE_BIN_LOG_LEVEL
        else:
            getattr(logging, log_level.upper(), logging.INFO)

        logging.basicConfig(
            level=log_level,
            datefmt="[%X]",
            handlers=[console_handler],
        )

    if "data_folder" in kwargs:
        folder = kwargs.pop("data_folder")
        ConstDataView(folder)

    func(**kwargs)


if __name__ == "__main__":
    main()
