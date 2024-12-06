import numpy as np

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arrows = ["^", ">", "v", "<"]

matrix_init = []
for line in lines:
    line = line.strip()
    matrix_init.append(list(line))

matrix = np.array(matrix_init)

row, col = np.where(np.isin(matrix, arrows))
arrow_index = (row[0], col[0])
start_index = arrow_index
arrow = arrows.index(matrix[arrow_index[0], arrow_index[1]])

max_rows, max_cols = matrix.shape

while True:
    i, j = arrow_index
    c = matrix[i, j]

    if c == "#":

        back_i = i - directions[arrow][0]
        back_j = j - directions[arrow][1]

        arrow_index = (back_i, back_j)

        arrow = (arrow + 1) % 4

    else:
        matrix[i, j] = "X"

        new_i = i + directions[arrow][0]
        new_j = j + directions[arrow][1]

        if 0 <= new_i < max_rows and 0 <= new_j < max_cols:
            arrow_index = (new_i, new_j)
        else:
            break


row, column = np.where(matrix == "X")

sum = 0

for r, c in zip(row, column):
    matrix_copy = np.array(matrix_init)
    matrix_copy[r][c] = "#"
    r, c = start_index

    seen = set()
    d = 0
    while True:
        if (r, c, d) in seen:
            sum += 1
            break
        seen.add((r, c, d))

        new_r = r + directions[d][0]
        new_c = c + directions[d][1]

        if not (0 <= new_r < max_rows and 0 <= new_c < max_cols):
            break

        if matrix_copy[new_r][new_c] == "#":
            d = (d + 1) % 4
        else:
            r, c = new_r, new_c


print(sum)
