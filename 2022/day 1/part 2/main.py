# https://adventofcode.com/2022/day/1
f = open("../input.txt", "r")
rations = list(map(lambda x: list(map(int, x.split('\n'))), f.read().split('\n\n')))

top = [0, 0, 0]


def new_score(score):
    for x in range(len(top)):
        if top[x] < score:
            tmp = top[x]
            top[x] = score
            new_score(tmp)
            break


for ration in rations:
    local_mx = 0
    for food in ration:
        local_mx += food
    new_score(local_mx)

print(sum(top), top)
