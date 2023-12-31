# https://adventofcode.com/2022/day/3
f = open("../input.txt", "r")
rucksacks = f.read().split('\n')

priority_sum = 0


def increase_priority(character):
    global priority_sum
    if character >= 'a':
        priority_sum += ord(character) % ord('a') + 1
        return
    priority_sum += ord(character) % ord('A') + 27


group_items = {}
group_count = 0
for sack in rucksacks:
    x, y = 0, len(sack) - 1
    x_items = {}
    y_items = {}
    while x < y:
        if sack[x] != sack[y]:
            if sack[x] not in y_items:
                if sack[x] not in x_items:
                    if sack[x] not in group_items:
                        group_items[sack[x]] = 1
                    else:
                        group_items[sack[x]] += 1
                    x_items[sack[x]] = 0
            if sack[y] not in x_items:
                if sack[y] not in y_items:
                    if sack[y] not in group_items:
                        group_items[sack[y]] = 1
                    else:
                        group_items[sack[y]] += 1
                    y_items[sack[y]] = 0
        x += 1
        y -= 1
    group_count += 1
    if group_count == 3:
        group_count = 0
        for k in group_items:
            if group_items[k] == 3:
                increase_priority(k)
                break
        group_items.clear()

print(priority_sum)
