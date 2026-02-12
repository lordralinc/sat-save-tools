import json
import pathlib
import typing

import pydantic
from argcomplete.completers import FilesCompleter

from sat_save_tools import ConstDataView, ItemPosition, SatisfactorySaveFile
from sat_save_tools.cli.utils import AnswerManager, add_input_file_action, set_completer

if typing.TYPE_CHECKING:
    import argparse


__all__ = ("setup",)


def export_somersloops(save_path: pathlib.Path, output: pathlib.Path | None = None) -> None:
    output = output or save_path.with_suffix(".somersloops.json")
    file = SatisfactorySaveFile.load_from_file(save_path)

    const_data = ConstDataView()
    somersloops = const_data.somersloop

    for level in file.body.full_levels:
        for collectable in [*(level.collectables or []), *(level.second_collectables or [])]:
            if collectable.path_name in somersloops:
                del somersloops[collectable.path_name]

    output.write_text(
        json.dumps(
            pydantic.TypeAdapter(dict[str, ItemPosition]).dump_python(somersloops, mode="json"),
            indent=2,
            ensure_ascii=False,
        ),
    )
    AnswerManager.success("export somersloops", f"File saved to {output}")


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    parser = subparsers.add_parser("export", help="Export somersloops data to JSON")
    add_input_file_action(parser)
    set_completer(
        parser.add_argument("--output", "-o", type=pathlib.Path, required=False, help="Path to the output JSON file"),
        FilesCompleter([".json"], directories=False),
    )
    parser.set_defaults(func=export_somersloops)
