# https://adventofcode.com/2022/day/12
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


def find_path(x, y, path: list = None):
    if path is None:
        path = [(x, y)]
    if terrain[x][y] == 'E':
        path_lengths.append(len(path))
        print(len(path), path)
        return
    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if new_x < 0 or new_x >= len(terrain) or new_y < 0 or new_y >= len(terrain[0]):
            continue
        current_terrain = terrain[x][y]
        new_terrain = terrain[new_x][new_y]
        if new_terrain == 'E':
            new_terrain = 'z'
        if ord(new_terrain) > ord(current_terrain) + 1 or (new_x, new_y) in path:
            continue
        path.append((new_x, new_y))
        find_path(new_x, new_y, path)
        path.pop()


from threading import Thread
threads = []
for x, row in enumerate(terrain):
    for y, col in enumerate(row):
        if col == 'S':
            terrain[x][y] = 'a'
            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                if new_x < 0 or new_x >= len(terrain) or new_y < 0 or new_y >= len(terrain[0]):
                    continue
                threads.append(Thread(target=find_path, args=(new_x, new_y, [(x, y), (new_x, new_y)])))
                threads[-1].start()
            break


for thread in threads:
    thread.join()
print(min(path_lengths) - 1)
