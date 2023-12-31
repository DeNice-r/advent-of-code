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



for sack in rucksacks:
    x, y = 0, len(sack) - 1
    # try with []
    x_items = {}
    y_items = {}
    while x < y:
        if sack[x] != sack[y]:
            if sack[x] not in y_items:
                x_items[sack[x]] = 1
            else:
                increase_priority(sack[x])
                # priority_sum += ord(sack[x]) % ord('a') + 1 - (6 if sack[x] >= 'A' else 0)
                break
            if sack[y] not in x_items:
                y_items[sack[y]] = 1
            else:
                increase_priority(sack[y])
                # priority_sum += ord(sack[y]) % ord('a') + 1 - (6 if sack[y] >= 'A' else 0)
                break
            x += 1
            y -= 1
            continue
        increase_priority(sack[x])
        # priority_sum += ord(sack[x]) % ord('a') + 1 - (6 if sack[x] >= 'A' else 0)
        break


print(priority_sum)
