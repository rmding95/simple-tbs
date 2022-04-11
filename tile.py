from abc import ABC, abstractmethod
from typing import Optional

from unit import Unit


class Tile(ABC):

    _defense: int
    _disallowed_units: Optional[list[str]]
    _terrain_cost: int
    _terrain: str
    _unit: Optional[Unit]

    def __init__(self):
        self._defense = 0
        self._terrain_cost = 0
        self._terrain = ""
        self._disallowed_units = None
        self._unit = None

    @property
    def defense(self) -> int:
        return self._defense

    @property
    def terrain_cost(self) -> int:
        return self._terrain_cost

    @property
    def disallowed_units(self) -> Optional[list[str]]:
        return self._disallowed_units

    @property
    def terrain(self) -> str:
        return self._terrain

    @abstractmethod
    def __repr__(self) -> str:
        return NotImplementedError()


class PlainsTile(Tile):
    def __init__(self):
        self._defense = 0
        self._terrain = "plains"
        self._terrain_cost = 0
        self._disallowed_units = None

    def __repr__(self) -> str:
        return "P"


class ForestTile(Tile):
    def __init__(self):
        self._defense = 0
        self._terrain = "forest"
        self._terrain_cost = 0
        self._disallowed_units = None

    def __repr__(self) -> str:
        return "F"


class RoadTile(Tile):
    def __init__(self):
        self._defense = 0
        self._terrain = "road"
        self._terrain_cost = 0
        self._disallowed_units = None

    def __repr__(self) -> str:
        return "="
