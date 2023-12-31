# https://adventofcode.com/2022/day/10
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
commands = f.read().split('\n')

cycle_num = 1
prev_x = 1
reg_x = 1
snapshots = [20, 60, 100, 140, 180, 220]
current_snapshot = 0
signal_strength_total = 0

for command in commands:
    if command == "noop":
        cycle_num += 1
        prev_x = reg_x
    else:
        prev_x = reg_x
        reg_x += int(command.split()[1])
        cycle_num += 2
    # print(f'{command} => {cycle_num} {reg_x}')
    if current_snapshot < len(snapshots) and snapshots[current_snapshot] <= cycle_num:
        if snapshots[current_snapshot] < cycle_num:
            print(current_snapshot, '|', cycle_num, prev_x)
            signal_strength_total += prev_x * snapshots[current_snapshot]
        else:
            print(current_snapshot, '|', cycle_num, reg_x)
            signal_strength_total += reg_x * snapshots[current_snapshot]
        current_snapshot += 1

print(signal_strength_total)
