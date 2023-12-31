# https://adventofcode.com/2022/day/8
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
forest = [list(map(int, line)) for line in f.read().split('\n')]
mx = 0
for x in range(1, len(forest) - 1):
    for y in range(1, len(forest[0]) - 1):
        score = 1
        current_score = 0
        for i in range(x + 1, len(forest)):
            current_score += 1
            if forest[i][y] >= forest[x][y]:
                break
        score *= current_score
        current_score = 0
        for j in range(y + 1, len(forest[0])):
            current_score += 1
            if forest[x][j] >= forest[x][y]:
                break
        score *= current_score
        current_score = 0
        for i in range(x - 1, -1, -1):
            current_score += 1
            if forest[i][y] >= forest[x][y]:
                break
        score *= current_score
        current_score = 0
        for j in range(y - 1, -1, -1):
            current_score += 1
            if forest[x][j] >= forest[x][y]:
                break
        score *= current_score
        if mx < score:
            mx = score

print(mx)


# Chat GPT answer (something to learn on situations where I would use 4 for loops):
# BTW it had two bugs that made its answers not even close to right, but AI refused to fix them without changing whole
# code, so I fixed them by myself.
def scenic_score(grid, r, c):
    score = 1
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        current_score = 0
        while 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            current_score += 1
            if grid[nr][nc] >= grid[r][c]:
                break
            nr, nc = nr + dr, nc + dc
        score *= current_score
    return score


def find_highest_scenic_score(grid):
    max_score = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            max_score = max(max_score, scenic_score(grid, r, c))
    return max_score


print(find_highest_scenic_score(forest))

