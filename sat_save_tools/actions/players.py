import typing

from sat_save_tools import HeaderType

if typing.TYPE_CHECKING:
    from sat_save_tools import (
        ActorObject,
        ArrayProperty,
        ComponentObject,
        ObjectReference,
        SatisfactorySaveFile,
        StrProperty,
    )


PLAYER_TYPE_PATH = "/Game/FactoryGame/Character/Player/BP_PlayerState.BP_PlayerState_C"


def get_player_list(sav_data: "SatisfactorySaveFile") -> "list[ActorObject]":
    levels = [*sav_data.body.levels, sav_data.body.persistent_level]

    players = []
    for level in levels:
        for obj in level.objects.values():
            if obj.header.type != HeaderType.ACTOR:
                continue
            if obj.header.type_path == PLAYER_TYPE_PATH:
                players.append(obj)
    return players


def get_player_nickname(sav_data: "SatisfactorySaveFile", player: "ActorObject") -> str | None:
    character = typing.cast("ObjectReference", player.properties.get_value("mOwnedPawn").value).get_related_object(
        sav_data,
    )
    nickname = typing.cast(
        "StrProperty | None",
        character.properties.get_value_or_none("mCachedPlayerName"),
    )
    return nickname.value if nickname is not None else None


def get_player_hotbars(sav_data: "SatisfactorySaveFile", player: "ActorObject") -> "list[ComponentObject]":
    hotbar = typing.cast("ArrayProperty", player.properties.get_value("mPlayerHotbars"))

    return [
        typing.cast("ComponentObject", it)
        for it in [typing.cast("ObjectReference", it).get_related_object(sav_data) for it in hotbar.value.elements]
        if it is not None
    ]
