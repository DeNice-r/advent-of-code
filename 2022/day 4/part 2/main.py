# https://adventofcode.com/2022/day/4
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
pairs = list(map(lambda x: list(map(lambda y: list(map(int, y.split('-'))), x)),
                 map(lambda x: x.split(','), f.read().split('\n'))))

overlap_count = 0

for pair in pairs:
    a, b = pair[0], pair[1]

    if b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1] or a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]:
        overlap_count += 1

print(overlap_count)
