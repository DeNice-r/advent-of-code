# https://adventofcode.com/2022/day/10
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
commands = f.read().split('\n')

cycle_num = 0
reg_x = 1
counter = 0
current_row = ''
command_idx = 0

while command_idx != len(commands):
    command = commands[command_idx]

    if command == "noop":
        counter = 0
        command_idx += 1
    else:
        counter += 1

    if reg_x - 1 <= cycle_num % 40 <= reg_x + 1:
        current_row += '#'
    else:
        current_row += '.'

    if counter == 2:
        reg_x += int(command.split()[1])
        counter = 0
        command_idx += 1

    cycle_num += 1
    if cycle_num % 40 == 0:
        print(current_row)
        current_row = ''


