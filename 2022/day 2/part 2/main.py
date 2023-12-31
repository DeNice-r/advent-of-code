# https://adventofcode.com/2022/day/2
f = open("../input.txt", "r")
turns = list(map(lambda x: x.split(' '), f.read().split('\n')))

score = 0

for turn in turns:
    score += ord(turn[1]) % ord('X') * 3
    if turn[1] == 'Y': # draw
        score += ord(turn[0]) - ord('A') + 1
    elif turn[1] == 'Z': # win
        score += (ord(turn[0]) + 1) % ord('A') % 3 + 1
    else:
        score += (ord(turn[0]) + 2) % ord('A') % 3 + 1


print(score)
