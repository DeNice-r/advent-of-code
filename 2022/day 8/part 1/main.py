# https://adventofcode.com/2022/day/8
from colorama import init, Fore, Style

debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
forest = f.read().split('\n')
draft = list(map(lambda x: list(x), forest[:]))


for x in range(len(forest)):
    mx = forest[x][0]
    draft[x][0] = '+'
    for y in range(len(forest[0])):
        if mx == 9:
            break
        if forest[x][y] > mx:
            draft[x][y] = '+'
            mx = forest[x][y]
for x in range(len(forest)):
    mx = forest[x][-1]
    draft[x][-1] = '+'
    for y in range(-1, -len(forest[0]), -1):
        if mx == 9:
            break
        if forest[x][y] > mx:
            draft[x][y] = '+'
            mx = forest[x][y]
for x in range(len(forest[0])):
    mx = forest[0][x]
    draft[0][x] = '+'
    for y in range(len(forest)):
        if mx == 9:
            break
        if forest[y][x] > mx:
            draft[y][x] = '+'
            mx = forest[y][x]
for x in range(-1, -len(forest[0]), -1):
    mx = forest[-1][x]
    draft[-1][x] = '+'
    for y in range(-1, -len(forest), -1):
        if mx == 9:
            break
        if forest[y][x] > mx:
            draft[y][x] = '+'
            mx = forest[y][x]


tree_num = 0
for x in range(len(draft)):
    for y in range(len(draft[x])):
        if draft[x][y] == '+':
            tree_num += 1
        print(f"{Fore.GREEN if draft[x][y] == '+' else Fore.RED}{forest[x][y]}",end='')
    print(Style.RESET_ALL)
    # print(f"{Fore.}{''.join(draft[x])}", forest[x])

print(tree_num)






