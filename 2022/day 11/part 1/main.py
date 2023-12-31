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

for raw_monkey in raw_monkeys:
    monkeys.append(Monkey(
        map(int, raw_monkey[0].split(':')[1].split(', ')),
        raw_monkey[1].split(':')[1].split('=')[1],
        int(raw_monkey[2].split()[-1]),
        int(raw_monkey[3].split()[-1]),
        int(raw_monkey[4].split()[-1]),
    ))

for x in range(20):
    print(x, '/'*100)
    for i, monkey in enumerate(monkeys):
        # monkey.inspection_count += len(monkey.items)
        for _ in range(len(monkey.items)):
            monkey.inspection_count += 1
            old = monkey.items[0]
            item_worry_level1 = eval(monkey.operation)
            item_worry_level2 = int(item_worry_level1 / 3)
            # print(item_worry_level)
            print(
                f'Monkey {i}:\n'
                f'Monkey inspects an item with a worry level of {old}.\n'
                f'Worry level is modified by formula: {monkey.operation} to {item_worry_level1}.\n'
                f'Monkey gets bored with item. Worry level is divided by 3 to {item_worry_level2}.'
            )
            if item_worry_level2 % monkey.divisible_by == 0:
                monkey.transfer_item_to(item_worry_level2, monkeys[monkey.if_throw_to])
                print(f'Current worry level is divisible by {monkey.divisible_by}.'
                      f'Item with worry level {item_worry_level2} is thrown to monkey {monkey.if_throw_to}.\n')
            else:
                monkey.transfer_item_to(item_worry_level2, monkeys[monkey.else_throw_to])
                print(f'Current worry level is not divisible by {monkey.divisible_by}.\n'
                      f'Item with worry level {item_worry_level2} is thrown to monkey {monkey.else_throw_to}.\n')


mx1 = monkeys[0].inspection_count
mx2 = mx1

for monkey in monkeys:
    if monkey.inspection_count > mx1:
        mx1 = monkey.inspection_count
    if mx2 < monkey.inspection_count != mx1:
        mx2 = monkey.inspection_count

print(mx1 * mx2)
