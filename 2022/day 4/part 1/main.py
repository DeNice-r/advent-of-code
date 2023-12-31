# https://adventofcode.com/2022/day/4
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
pairs = list(map(lambda x: list(map(lambda y: list(map(int, y.split('-'))), x)),
                 map(lambda x: x.split(','), f.read().split('\n'))))

containment_count = 0

for pair in pairs:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1] or \
            pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        containment_count += 1

print(containment_count)
