import enum
import pathlib
import typing

import pydantic
from pydantic_core import to_json

from sat_save_tools.utils import pydantic_eq

if typing.TYPE_CHECKING:
    from .models.properties.typed_data import DoubleQuaternion, DoubleVector3

__all__ = (
    "ConstDataView",
    "FreeDroppedItem",
    "ItemPosition",
    "Purity",
    "ResourcePurity",
)


@pydantic_eq
class ItemPosition(pydantic.BaseModel):
    level_name: str
    rotation: "DoubleQuaternion"
    position: "DoubleVector3"


@pydantic_eq
class FreeDroppedItem(pydantic.BaseModel):
    quantity: int
    location: "DoubleVector3"
    instance_name: str


class Purity(enum.IntEnum):
    UNKNOWN = 0
    IMPURE = 1
    NORMAL = 2
    PURE = 3


@pydantic_eq
class ResourcePurity(pydantic.BaseModel):
    name: str
    purity: Purity


class ConstDataView:
    """
    Cached read-only data accessor with conditional instance reuse.

    Instance behavior rules:

    - The class maintains a single globally stored instance.
    - A new instance is created if:
        * no instance exists yet, or
        * the currently stored instance was created with a target folder
          that is neither:
              - the requested `target_folder`, nor
              - the default data folder.

    - If the existing instance was created with:
        * the same `target_folder`, or
        * the default folder,
      then it is reused.

    In effect:
    - The default-path instance is treated as compatible with any request.
    - A non-default instance is replaced when switching to a different
      non-default path.
    - Only one instance is retained at any time.

    Notes:
    - Instance selection logic lives entirely in `__new__`.
    - This design assumes controlled, single-threaded usage.
    """

    _instance: "ConstDataView | None" = None
    _default_path = (pathlib.Path(__file__).parent.parent / "data").resolve()

    target_folder: pathlib.Path
    _cache: dict[str, typing.Any]

    def __new__(
        cls,
        target_folder: pathlib.Path | None = None,
    ) -> typing.Self:
        path = (target_folder or cls._default_path).resolve()

        if not cls._instance or (cls._instance.target_folder not in {path, cls._default_path}):
            inst = super().__new__(cls)
            inst.target_folder = path
            inst._cache = {}
            cls._default_instance = inst
        return cls._default_instance

    def get_item[T](
        self,
        file: pathlib.Path,
        type_adapter: pydantic.TypeAdapter[T],
    ) -> T:
        """
        Load, validate, and cache structured data from a file.

        The file is parsed only once per instance. Parsed values are
        stored in an internal cache keyed by file name.

        :param file: Path to the input file.
        :param type_adapter: Pydantic TypeAdapter used for validation and deserialization.
        :return: A validated object of type `T`.
        """
        if file.name not in self._cache:
            self._cache[file.name] = type_adapter.validate_json(file.read_bytes())
        return self._cache[file.name]

    @property
    def crash_sites(self) -> dict[str, ItemPosition]:
        return self.get_item(
            self.target_folder / "crash_sites.json",
            pydantic.TypeAdapter(dict[str, ItemPosition]),
        )

    @property
    def conveyor_belts(self) -> list[str]:
        return self.get_item(
            self.target_folder / "conveyor_belts.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def free_dropped_items(self) -> dict[str, list[FreeDroppedItem]]:
        return self.get_item(
            self.target_folder / "free_dropped_items.json",
            pydantic.TypeAdapter(dict[str, list[FreeDroppedItem]]),
        )

    @property
    def hotbar_path_name_customization_recipes(self) -> list[str]:
        return self.get_item(
            self.target_folder / "hotbar_path_name_customization_recipes.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def hotbar_path_name_emotes(self) -> list[str]:
        return self.get_item(
            self.target_folder / "hotbar_path_name_emotes.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def hotbar_path_name_recipes(self) -> list[str]:
        return self.get_item(
            self.target_folder / "hotbar_path_name_recipes.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def icon_ids(self) -> dict[str, int]:
        return self.get_item(
            self.target_folder / "icon_ids.json",
            pydantic.TypeAdapter(dict[str, int]),
        )

    @property
    def items_for_player_inventory(self) -> list[str]:
        return self.get_item(
            self.target_folder / "items_for_player_inventory.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def mercer_spheres(self) -> dict[str, ItemPosition]:
        return self.get_item(
            self.target_folder / "mercer_spheres.json",
            pydantic.TypeAdapter(dict[str, ItemPosition]),
        )

    @property
    def milestone_costs(self) -> dict[str, dict[str, int]]:
        return self.get_item(
            self.target_folder / "milestone_costs.json",
            pydantic.TypeAdapter(dict[str, dict[str, int]]),
        )

    @property
    def mined_resources(self) -> list[str]:
        return self.get_item(
            self.target_folder / "mined_resources.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def miners(self) -> list[str]:
        return self.get_item(
            self.target_folder / "miners.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def power_line(self) -> list[str]:
        return self.get_item(
            self.target_folder / "power_line.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def power_slug(self) -> list[str]:
        return self.get_item(
            self.target_folder / "power_slug.json",
            pydantic.TypeAdapter(list[str]),
        )

    @property
    def power_slugs(
        self,
    ) -> 'dict[typing.Literal["blue", "yellow", "purple"], dict[str, DoubleVector3]]':
        return self.get_item(
            self.target_folder / "power_slug.json",
            pydantic.TypeAdapter(
                'dict[typing.Literal["blue", "yellow", "purple"], dict[str, DoubleVector3]]',
            ),
        )

    @property
    def project_assembly_costs(self) -> dict[str, dict[str, int]]:
        return self.get_item(
            self.target_folder / "project_assembly_costs.json",
            pydantic.TypeAdapter(dict[str, dict[str, int]]),
        )

    @property
    def readable_names(self) -> dict[str, str]:
        return self.get_item(
            self.target_folder / "readable_names.json",
            pydantic.TypeAdapter(dict[str, str]),
        )

    @property
    def resource_purity(self) -> dict[str, ResourcePurity]:
        return self.get_item(
            self.target_folder / "resource_purity.json",
            pydantic.TypeAdapter(dict[str, ResourcePurity]),
        )

    @property
    def somersloop(self) -> dict[str, ItemPosition]:
        return self.get_item(
            self.target_folder / "somersloop.json",
            pydantic.TypeAdapter(dict[str, ItemPosition]),
        )

    @property
    def unlock_paths(self) -> dict[str, list[str]]:
        return self.get_item(
            self.target_folder / "unlock_paths.json",
            pydantic.TypeAdapter(dict[str, list[str]]),
        )

    def export_json(self, target_folder: pathlib.Path) -> None:
        target_folder.mkdir(parents=True, exist_ok=True)

        self.crash_sites  # noqa: B018
        self.conveyor_belts  # noqa: B018
        self.free_dropped_items  # noqa: B018
        self.hotbar_path_name_customization_recipes  # noqa: B018
        self.hotbar_path_name_emotes  # noqa: B018
        self.hotbar_path_name_recipes  # noqa: B018
        self.icon_ids  # noqa: B018
        self.items_for_player_inventory  # noqa: B018
        self.mercer_spheres  # noqa: B018
        self.milestone_costs  # noqa: B018
        self.mined_resources  # noqa: B018
        self.miners  # noqa: B018
        self.power_line  # noqa: B018
        self.power_slug  # noqa: B018
        self.power_slugs  # noqa: B018
        self.project_assembly_costs  # noqa: B018
        self.readable_names  # noqa: B018
        self.resource_purity  # noqa: B018
        self.somersloop  # noqa: B018
        self.unlock_paths  # noqa: B018

        for file_name, data in self._cache.items():
            (target_folder / file_name).write_bytes(
                to_json(data, indent=2, ensure_ascii=False),
            )
