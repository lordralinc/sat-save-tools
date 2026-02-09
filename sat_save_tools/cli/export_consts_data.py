import pathlib
from argparse import ArgumentParser, _SubParsersAction

import rich
import rich.panel
from rich.text import Text

from sat_save_tools.cli.answers import AnswerManager
from sat_save_tools.data import ConstDataView

console = rich.console.Console()


def export_consts_data_command(foldername: pathlib.Path):
    data_view = ConstDataView()
    data_view.export_json(foldername)
    AnswerManager.success(
        "export results",
        Text.assemble(
            Text("✅ Export completed!\n", style="bold green"),
            Text(f"All files have been saved to: {foldername}", style="cyan"),
        ),
    )


def setup(
    subparsers: _SubParsersAction[ArgumentParser],
):
    parser = subparsers.add_parser("export-consts-data", help="Save JSON consts data to folder")
    parser.add_argument("foldername", type=pathlib.Path, help="Path to the save file")
    parser.set_defaults(func=export_consts_data_command)
