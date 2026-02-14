import json
import pathlib
import typing

import rich
import rich.table
from argcomplete.completers import FilesCompleter

from sat_save_tools import ComponentObject, SatisfactorySaveFile
from sat_save_tools.actions.players import get_player_list, get_player_nickname
from sat_save_tools.cli.utils import AnswerManager, add_input_file_action, add_output_file_action, set_completer

if typing.TYPE_CHECKING:
    import argparse

    from sat_save_tools import (
        ArrayElementStruct,
        InventoryItem,
        ObjectReference,
        PropertyList,
    )

__all__ = ("setup",)


def show_player_inventory(save_path: pathlib.Path, player_id: str) -> None:
    file = SatisfactorySaveFile.load_from_json(save_path)
    players = get_player_list(file)

    player = next((it for it in players if it.header.instance_name == player_id), None)
    if player is None:
        return AnswerManager.error("player inventory", f"Player with ID '{player_id}' not found")

    player_nickname = get_player_nickname(file, player) or player_id

    owner_pawn = typing.cast("ObjectReference", player.properties.get_value("mOwnedPawn").value).get_related_object(
        file,
    )
    inventory = typing.cast(
        "ObjectReference",
        owner_pawn.properties.get_value("mInventory").value,
    ).get_related_object(file)

    inventory_stacks = typing.cast(
        "list[PropertyList]",
        typing.cast(
            "ArrayElementStruct",
            inventory.properties.get_value("mInventoryStacks").value,
        ).elements,
    )

    table = rich.table.Table(show_lines=True)
    table.add_column("Item ID", style="bold cyan")
    table.add_column("Num items", style="magenta")

    for stack in inventory_stacks:
        item = typing.cast("InventoryItem", stack.get_value("Item").value)
        quantity = typing.cast("int", stack.get_value("NumItems").value)
        if item.name:
            table.add_row(item.name, str(quantity))
    AnswerManager.success(f"inventory items for player {player_nickname}", table)


def export_player_inventory(
    save_path: pathlib.Path,
    player_id: str,
    output: pathlib.Path | None = None,
) -> None:
    file = SatisfactorySaveFile.load_from_json(save_path)
    output = output or save_path.parent.with_suffix(f".{player_id}_inventory.json")
    players = get_player_list(file)

    player = next((it for it in players if it.header.instance_name == player_id), None)
    if player is None:
        return AnswerManager.error("player inventory", f"Player with ID '{player_id}' not found")

    player_nickname = get_player_nickname(file, player) or player_id
    owner_pawn = typing.cast("ObjectReference", player.properties.get_value("mOwnedPawn").value).get_related_object(
        file,
    )
    inventory = typing.cast(
        "ObjectReference",
        owner_pawn.properties.get_value("mInventory").value,
    ).get_related_object(file)

    output.write_text(
        json.dumps(inventory.model_dump(mode="json"), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    AnswerManager.success(f"export inventory for player {player_nickname}", f"exported to {output}")


def import_player_inventory(
    save_path: pathlib.Path,
    inventory_path: pathlib.Path,
    player_id: str,
    output: pathlib.Path | None = None,
) -> None:
    file = SatisfactorySaveFile.load_from_json(save_path)
    output = output or save_path

    players = get_player_list(file)

    player = next((it for it in players if it.header.instance_name == player_id), None)
    if player is None:
        return AnswerManager.error("player inventory", f"Player with ID '{player_id}' not found")
    owner_pawn = typing.cast("ObjectReference", player.properties.get_value("mOwnedPawn").value).get_related_object(
        file,
    )
    current_inventory = typing.cast(
        "ComponentObject",
        typing.cast(
            "ObjectReference",
            owner_pawn.properties.get_value("mInventory").value,
        ).get_related_object(file),
    )

    new_inventory = ComponentObject.model_validate_json(inventory_path.read_text(encoding="utf-8"))

    new_inventory.header.instance_name = current_inventory.header.instance_name
    new_inventory.header.unknown = current_inventory.header.unknown
    new_inventory.header.parent_actor_name = current_inventory.header.parent_actor_name

    file.body.persistent_level.objects[current_inventory.header.instance_name] = new_inventory

    file.save_to_file(output)
    AnswerManager.success("import inventory", f"File saved to {output}")


def setup(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]"):
    inventory_parser = subparsers.add_parser("inventory", help="Player inventories commands")
    inventory_subparsers = inventory_parser.add_subparsers(required=True)

    show_inventory_parser = inventory_subparsers.add_parser("show", help="Show player inventory")
    add_input_file_action(show_inventory_parser)
    show_inventory_parser.add_argument("--player-id", type=str, help="Player ID to show inventory for", required=True)
    show_inventory_parser.set_defaults(func=show_player_inventory)

    export_inventory_parser = inventory_subparsers.add_parser("export", help="Export player inventory")
    add_input_file_action(export_inventory_parser)
    export_inventory_parser.add_argument("--player-id", type=str, help="Player ID to export inventory", required=True)
    set_completer(
        export_inventory_parser.add_argument(
            "--output",
            "-o",
            type=pathlib.Path,
            help="Output file",
            required=False,
        ),
        FilesCompleter([".json"], directories=False),
    )
    export_inventory_parser.set_defaults(func=export_player_inventory)

    import_inventory_parser = inventory_subparsers.add_parser("import", help="Import player inventory")
    add_input_file_action(import_inventory_parser)
    set_completer(
        import_inventory_parser.add_argument("--inventory-path", "-i", type=pathlib.Path, help="Path to the JSON file"),
        FilesCompleter([".json"], directories=False),
    )
    import_inventory_parser.add_argument("--player-id", type=str, help="Player ID to import inventory", required=True)
    add_output_file_action(import_inventory_parser)
    import_inventory_parser.set_defaults(func=import_player_inventory)
