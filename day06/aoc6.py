import numpy as np

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

directions = [(-1,0),(0,1),(1,0),(0,-1)]
arrows = ["^", ">", "v", "<"]

matrix = []
for line in lines:
    line = line.strip()
    matrix.append(list(line))

matrix = np.array(matrix)

row, col = np.where(np.isin(matrix, arrows))
arrow_index = (row[0], col[0])
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


print(np.count_nonzero(matrix == "X"))