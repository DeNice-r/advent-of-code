# https://adventofcode.com/2022/day/9
debug = False
f = open("../debug_input2.txt" if debug else "../input.txt", "r")
commands = map(lambda x: [x.split()[0], int(x.split()[1])], f.read().split('\n'))

rope = [[0, 0] for x in range(10)]
visited = {(0, 0)}
directions = {
    'U': [0, 1],
    'R': [1, 0],
    'D': [0, -1],
    'L': [-1, 0],
}

for command in commands:
    for _ in range(command[1]):
        rope[0][0] += directions[command[0]][0]
        rope[0][1] += directions[command[0]][1]

        for x in range(1, 10):
            if rope[x-1][0] != rope[x][0]:
                if rope[x-1][1] != rope[x][1] and abs(rope[x-1][0] - rope[x][0]) + abs(rope[x-1][1] - rope[x][1]) > 2:
                    rope[x][0] += (rope[x-1][0] > rope[x][0]) - (rope[x-1][0] < rope[x][0])
                    rope[x][1] += (rope[x-1][1] > rope[x][1]) - (rope[x-1][1] < rope[x][1])
                elif abs(rope[x-1][0] - rope[x][0]) > 1:
                    rope[x][0] += (rope[x-1][0] > rope[x][0]) - (rope[x-1][0] < rope[x][0])
            elif rope[x-1][1] != rope[x][1] and abs(rope[x-1][1] - rope[x][1]) > 1:
                rope[x][1] += (rope[x-1][1] > rope[x][1]) - (rope[x-1][1] < rope[x][1])
        visited.add(tuple(rope[-1]))


print(len(visited))
