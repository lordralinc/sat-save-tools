import pathlib
import typing
from argparse import ArgumentParser, _SubParsersAction

import rich
import rich.panel

from sat_save_tools.satisfactory_save import SatisfactorySaveFile

if typing.TYPE_CHECKING:
    import jinja2

console = rich.console.Console(record=True)


def get_jinja_env() -> "jinja2.Environment":
    import jinja2  # noqa: PLC0415

    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(pathlib.Path(__file__).parent.parent.parent / "data" / "jinja_templates"),
        autoescape=jinja2.select_autoescape(["html", "xml"]),
    )


def to_html_command(filename: pathlib.Path, output: pathlib.Path | None = None) -> None:
    if not filename.exists():
        console.print(f"File {filename} does not exist", style="bold red")
        return
    output = output or filename.with_suffix(".html")

    file = SatisfactorySaveFile.load_from_file(filename)

    template = get_jinja_env().get_template("main.jinja2")
    output.write_text(template.render(file=file))
    console.print(
        rich.panel.Panel(
            f"Saved to {output}",
            title="[bold white]HTML Result[/]",
            border_style="green",
            expand=False,
        ),
    )


def setup(
    subparsers: _SubParsersAction[ArgumentParser],
):
    try:
        import jinja2  # noqa: F401, PLC0415
    except ImportError:
        return
    else:
        parser = subparsers.add_parser("html", help="Generate HTML")
        parser.add_argument("filename", type=pathlib.Path, help="Path to the save file")
        parser.add_argument(
            "--output",
            "-o",
            type=pathlib.Path,
            required=False,
            help="Path to output JSON file; if not set, saved in {input}.html",
        )
        parser.set_defaults(func=to_html_command)
