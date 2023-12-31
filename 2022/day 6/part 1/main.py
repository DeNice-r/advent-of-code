# https://adventofcode.com/2022/day/6
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
data = f.read()


def unique(l: str):
    return l == ''.join(dict.fromkeys(l).keys())


for x in range(len(data) - 4):
    if unique(data[x:x+4]):
        print(x+4)
        break
