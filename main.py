from game_map import create_map

MAP_LENGTH = 25
MAP_WIDTH = 10


def main():
    map = create_map(MAP_LENGTH, MAP_WIDTH)
    while True:
        print(map.draw_map())
        s = ""
        while True:
            s = input("Select a tile\n")
            if len(s) == 2:
                break
        tile = map.select_tile(s[0], int(s[1]))
        print(f"Selected {tile.terrain} tile at {s[0]}{s[1]}")


if __name__ == "__main__":
    main()
