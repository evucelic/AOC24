import numpy as np

input_path = "input.txt"

input = open(input_path, "r").read().split("\n\n")

grid = input[0].split("\n")
moves = []
for m in input[1].split("\n"):
    for c in m:
        moves.append(c)

for i,l in enumerate(grid):
    grid[i] = [c for c in l]

grid = np.array(grid)
m = len(grid)
n = len(grid[0])

i,j = np.where(grid == "@")
i,j = *i, *j
grid[i][j] = "."

for dir in moves:
    if dir == '<':
        k = j-1
        while grid[i][k] == 'O':
            k -= 1
        if grid[i][k] == '.':
            grid[i][k], grid[i][j-1] = grid[i][j-1], grid[i][k]
            i,j = i, j-1

    elif dir == '>':
        k = j+1
        while grid[i][k] == 'O':
            k += 1
        if grid[i][k] == '.':
            grid[i][k], grid[i][j+1] = grid[i][j+1], grid[i][k]
            i,j = i, j+1

    elif dir == '^':
        k = i-1
        while grid[k][j] == 'O':
            k -= 1
        if grid[k][j] == '.':
            grid[k][j], grid[i-1][j] = grid[i-1][j], grid[k][j]
            i,j = i-1, j

    elif dir == 'v':
        k = i+1
        while grid[k][j] == 'O':
            k += 1
        if grid[k][j] == '.':
            grid[k][j], grid[i+1][j] = grid[i+1][j], grid[k][j]
            i,j = i+1, j

total = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'O':
            total += 100*i + j

print(total)