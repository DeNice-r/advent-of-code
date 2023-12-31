# https://adventofcode.com/2022/day/12

from threading import Thread
from timeit import timeit


debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
terrain: list[list[str]] = list(map(list, f.read().split('\n')))


directions = [
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0)
]
path_lengths = []


def find_path(path: list):
    x, y = path[-1]
    if terrain[x][y] == 'S':
        path_lengths.append(len(path))
        # print(len(path), path)
        return
    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if new_x < 0 or new_x >= len(terrain) or new_y < 0 or new_y >= len(terrain[0]):
            continue

        # if (new_x, new_y) == path[-2]:
        #     continue

        current_terrain = terrain[x][y]
        new_terrain = terrain[new_x][new_y]
        if new_terrain == 'S':
            new_terrain = 'a'
        if ord(new_terrain) < ord(current_terrain) - 1 or (new_x, new_y) in path:
            continue
        path.append((new_x, new_y))
        find_path(path)
        path.pop()


def main():
    threads = []
    for x, row in enumerate(terrain):
        for y, col in enumerate(row):
            if col == 'E':
                terrain[x][y] = 'z'
                find_path([(x, y)])

    # for thread in threads:
    #     thread.join()

    print(min(path_lengths) - 1)


# n = 1000000
# print(timeit("main()", globals=globals(), number=n))
main()
