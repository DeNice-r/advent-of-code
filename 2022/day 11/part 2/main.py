# https://adventofcode.com/2022/day/11
import math

debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
raw_monkeys = map(lambda x: x.split('\n')[1:], f.read().split('\n\n'))


class Monkey:
    def __init__(self, starting_items, operation, divisible_by, if_throw_to, else_throw_to):
        self.items = list(starting_items)
        self.operation = operation
        self.divisible_by = divisible_by
        self.if_throw_to = if_throw_to
        self.else_throw_to = else_throw_to
        self.inspection_count = 0

    def transfer_item_to(self, new_value, to_monkey):
        del self.items[0]
        to_monkey.items.append(new_value)


monkeys = []
lcm = 1

for raw_monkey in raw_monkeys:
    monkeys.append(Monkey(
        map(int, raw_monkey[0].split(':')[1].split(', ')),
        raw_monkey[1].split(':')[1].split('=')[1],
        int(raw_monkey[2].split()[-1]),
        int(raw_monkey[3].split()[-1]),
        int(raw_monkey[4].split()[-1]),
    ))
    lcm *= monkeys[-1].divisible_by

for x in range(10000):
    print(x, '/'*100)
    for i, monkey in enumerate(monkeys):
        monkey.inspection_count += len(monkey.items)
        for _ in range(len(monkey.items)):
            old = monkey.items[0]
            item_worry_level = eval(monkey.operation)
            item_worry_level %= lcm
            if item_worry_level % monkey.divisible_by == 0:
                monkey.transfer_item_to(item_worry_level, monkeys[monkey.if_throw_to])
            else:
                monkey.transfer_item_to(item_worry_level, monkeys[monkey.else_throw_to])


mx1 = monkeys[0].inspection_count
mx2 = 0


for monkey in monkeys:
    if monkey.inspection_count > mx1:
        mx2 = mx1
        mx1 = monkey.inspection_count
    elif monkey.inspection_count > mx2:
        mx2 = monkey.inspection_count


print(mx1 * mx2)
