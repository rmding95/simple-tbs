from abc import ABC, abstractmethod


class Unit(ABC):

    _name: str
    _cost: int
    _movement: int
    _health: int
    _damage: int

    def __init__(self):
        self._name = ""
        self._cost = 0
        self._movement = 0
        self._health = 0
        self._damage = 0

    @abstractmethod
    def __repr__(self) -> str:
        return NotImplementedError()


class Infantry(Unit):
    def __init__(self):
        self._name = "Infantry"
        self._cost = 100
        self._movement = 2
        self._health = 10
        self._damage = 10

    def __repr__(self) -> str:
        return "I"


class Tank(Unit):
    def __init__(self):
        self._name = "Tank"
        self._cost = 500
        self._movement = 5
        self._health = 50
        self._damage = 50

    def __repr__(self) -> str:
        return "T"
