from string import ascii_uppercase

from tile import PlainsTile, ForestTile, RoadTile, Tile

SPACING = 4


class GameMap:

    length: int
    width: int
    map: list[list[Tile]]

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.map = [[PlainsTile() for _ in range(length)] for _ in range(width)]

    def __repr__(self) -> str:
        s = ""
        for row in self.map:
            s += f"{' '.join(str(row))}\n"
        return s

    def select_tile(self, row: str, col: int) -> Tile:
        ord_num = ord(row)
        assert ord_num >= 65, ord_num
        assert ord_num <= 90, ord_num
        return self.map[col][ord_num - ord("A")]

    def draw_map(self) -> str:
        s = f"{' '*(SPACING + 1)}"
        for letter in ascii_uppercase[: self.length]:
            s += f"{letter}{' '*SPACING}"
        s += "\n"
        for i in range(1, self.width):
            s += f"{i}{' '*SPACING}"
            for tile in self.map[i - 1]:
                s += f"{str(tile)}{' '*SPACING}"
            s += "\n"
        return s


def create_map(length: int, width: int) -> GameMap:
    return GameMap(length, width)
