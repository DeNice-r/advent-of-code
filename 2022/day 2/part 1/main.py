# https://adventofcode.com/2022/day/2
f = open("../input.txt", "r")
turns = list(map(lambda x: x.split(' '), f.read().split('\n')))

score = 0

for turn in turns:
    score += ord(turn[1]) % ord('X') + 1
    if ord(turn[0]) % ord('A') == ord(turn[1]) % ord('X'):
        score += 3
        continue
    if ord(turn[1]) % ord('X') == (ord(turn[0]) % ord('A') + 1) % 3:
        score += 6


print(score)
