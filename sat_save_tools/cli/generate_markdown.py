import argparse
import pathlib
import re
from functools import partial

CLI_HEADER = "## Command-Line Interface (CLI)"
LIB_HEADER = "## Using as a Library"
ANSI_ESCAPE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")


def strip_ansi(text: str) -> str:
    return ANSI_ESCAPE.sub("", text)


def generate_toc(parser: argparse.ArgumentParser, parent: str = "", level: int = 0) -> list[str]:
    lines: list[str] = []

    subparsers = next(
        (a for a in parser._actions if isinstance(a, argparse._SubParsersAction)),  # noqa: SLF001
        None,
    )

    if not subparsers:
        return lines

    indent = "  " * level

    for name, sub in subparsers.choices.items():
        full = f"{parent} {name}".strip()
        anchor = full.lower().replace(" ", "-")

        lines.append(f"{indent}- [`{full}`](#{anchor})")
        lines.extend(generate_toc(sub, full, level + 1))

    return lines


def generate_cli_markdown(parser: argparse.ArgumentParser, parent_cmd: str = "") -> str:
    lines: list[str] = []

    cmd_name = parent_cmd or parser.prog

    usage = strip_ansi(parser.format_usage().strip())
    lines.append("```bash")
    lines.append(usage)
    lines.append("```")
    lines.append("")

    subparsers_action = next(
        (a for a in parser._actions if isinstance(a, argparse._SubParsersAction)),  # noqa: SLF001
        None,
    )

    if parser._actions:  # noqa: SLF001
        arg_lines = []
        for action in parser._actions:  # noqa: SLF001
            if isinstance(action, argparse._SubParsersAction):  # noqa: SLF001
                continue
            if action.option_strings and action.option_strings[0] not in ("-h", "--help"):
                opts = ", ".join(action.option_strings)
                req = " (required)" if action.required else ""
                default = f" [default: {action.default}]" if action.default not in (None, False, "==SUPPRESS==") else ""
                arg_lines.append(f"- `{opts}`: {strip_ansi(action.help or '')}{req}{default}")
            elif action.dest != "help":
                arg_lines.append(f"- `{action.dest}`: {strip_ansi(action.help or '')}")

        if arg_lines:
            lines.append("**Arguments:**")
            lines.extend(arg_lines)
            lines.append("")

    if subparsers_action:
        lines.append("### Subcommands")
        for sub_name, subparser in subparsers_action.choices.items():
            if parent_cmd != "":
                lines.append(f"#### `{cmd_name.replace('python.exe -m sat_save_tools ', '')} {sub_name}`")
            else:
                lines.append(f"#### `{sub_name}`")
            sub_md = generate_cli_markdown(subparser, parent_cmd=f"{cmd_name} {sub_name}")
            lines.append(sub_md)
            lines.append("")
    if parent_cmd == "":
        toc = generate_toc(parser)
        return "\n".join(toc) + "\n\n" + "\n".join(lines).rstrip().replace("python.exe ", "python ")
    return "\n".join(lines).rstrip().replace("python.exe ", "python ")


def cmd_gen_cli_docs(readme: pathlib.Path, parser: argparse.ArgumentParser) -> None:
    text = readme.read_text(encoding="utf-8")

    start = text.find(CLI_HEADER)
    end = text.find(LIB_HEADER)

    if start == -1 or end == -1 or start >= end:
        raise RuntimeError("Cannot find CLI section boundaries in README.md")

    generated_cli = generate_cli_markdown(parser)

    new_text = text[: start + len(CLI_HEADER)] + "\n\n" + generated_cli.rstrip() + "\n\n" + text[end:]

    readme.write_text(new_text, encoding="utf-8")


def setup(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
    main_parser: argparse.ArgumentParser,
) -> None:
    parser = subparsers.add_parser(
        "gen-cli-docs",
        help="Generate CLI documentation section in README.md",
    )
    parser.add_argument(
        "--readme",
        type=pathlib.Path,
        default=pathlib.Path("README.md"),
        help="Path to README.md",
    )
    parser.set_defaults(func=partial(cmd_gen_cli_docs, parser=main_parser))
