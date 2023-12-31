# https://adventofcode.com/2022/day/5
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
raw_stacks, raw_commands = f.read().split('\n\n')

raw_commands = raw_commands.split('\n')
commands = list(map(lambda x: list(map(int, x.split()[1::2])), raw_commands))

raw_stacks = raw_stacks.split('\n')
stacks = {}
for x in list(zip(*raw_stacks[::-1]))[1::4]:
    stacks[int(x[0])] = [x for x in x[1:] if x != ' ']

for x in commands:
    for _ in range(x[0]):
        stacks[x[2]].append(stacks[x[1]].pop())

for x in stacks:
    print(stacks[x].pop(), end='')

