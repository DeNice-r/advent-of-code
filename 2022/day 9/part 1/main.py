# https://adventofcode.com/2022/day/9
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
commands = map(lambda x: [x.split()[0], int(x.split()[1])], f.read().split('\n'))

h, t, visited = [0, 0], [0, 0], {(0, 0)}
directions = {
    'U': [0, 1],
    'R': [1, 0],
    'D': [0, -1],
    'L': [-1, 0],
}

for command in commands:
    for x in range(command[1]):
        h[0] += directions[command[0]][0]
        h[1] += directions[command[0]][1]

        if h[0] != t[0]:
            if h[1] != t[1] and abs(h[0] - t[0]) + abs(h[1] - t[1]) > 2:
                t[0] += (h[0] > t[0]) - (h[0] < t[0])
                t[1] += (h[1] > t[1]) - (h[1] < t[1])
            elif abs(h[0] - t[0]) > 1:
                t[0] += (h[0] > t[0]) - (h[0] < t[0])
        elif h[1] != t[1] and abs(h[1] - t[1]) > 1:
            t[1] += (h[1] > t[1]) - (h[1] < t[1])
        visited.add(tuple(t))


print(len(visited))
