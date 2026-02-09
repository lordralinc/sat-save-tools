import pathlib
from argparse import ArgumentParser, _SubParsersAction

from rich.table import Table

from sat_save_tools import ConstDataView, DoubleVector3, SatisfactorySaveFile
from sat_save_tools.cli.answers import AnswerManager

__all__ = ("setup",)


def find_free_staff_command(filename: pathlib.Path | None, item: str | None = None) -> None:
    data_view = ConstDataView()
    if not item:
        table = Table(show_lines=True)

        table.add_column("Item", style="bold cyan")
        table.add_column("Total quantity", style="green")

        for item_name, item_v in data_view.free_dropped_items.items():
            table.add_row(item_name, str(sum(it.quantity for it in item_v)))
        AnswerManager.success("Free dropped items", table)
        return

    dropped_instances: dict[str, tuple[int, DoubleVector3]] = {}

    for item_name, items in data_view.free_dropped_items.items():
        if item_name == item:
            for it in items:
                dropped_instances[it.instance_name] = (it.quantity, it.location)
            break

    if not dropped_instances:
        AnswerManager.error("Free dropped items", f"No free {item} found")
        return
    if filename is not None:
        save = SatisfactorySaveFile.load_from_file(filename)

        collected = set()
        for level in save.body.levels:
            if level.collectables:
                collected.update(c.path_name for c in level.collectables)

        dropped_instances = {name: data for name, data in dropped_instances.items() if name not in collected}

        if not dropped_instances:
            AnswerManager.success("Free dropped items", f"[yellow]All {item} already collected[/yellow]")
            return

    table = Table(show_lines=True)
    table.add_column("Quantity", justify="right", style="green")
    table.add_column("Position", style="cyan")

    total = 0
    for quantity, position in dropped_instances.values():
        table.add_row(
            str(quantity),
            f"X = {position.x:.1f}, Y = {position.y:.1f}, Z = {position.z:.1f}",
        )
        total += quantity
    AnswerManager.success("Free dropped items", table)


def setup(subparsers: _SubParsersAction[ArgumentParser]):
    parser = subparsers.add_parser(
        "find-free-stuff",
        help="Show free stuff in save file",
        description=(
            "Displays all free/uncollected items in a save file.\n"
            "If --item is provided, shows detailed locations of that item."
        ),
    )
    parser.add_argument(
        "--filename",
        "-f",
        type=pathlib.Path,
        help="Path to the save file",
        required=False,
    )
    parser.add_argument("--item", "-i", type=str, required=False)
    parser.set_defaults(func=find_free_staff_command)
