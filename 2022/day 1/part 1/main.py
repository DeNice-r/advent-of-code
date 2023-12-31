# https://adventofcode.com/2022/day/1
import sys

max_calories = -sys.maxsize
current_elf_calories = 0

with open('../input.txt', 'r') as f:
    for line in f:
        if line.strip() == "":
            if current_elf_calories > max_calories:
                max_calories = current_elf_calories
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)
    if current_elf_calories > max_calories:
        max_calories = current_elf_calories

print(f"The Elf carrying the most Calories has {max_calories} total Calories.")