import numpy as np

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

count = 0

matrix = []

for line in lines:
    l = list(line.strip())
    matrix.append(l)

x, y = len(matrix), len(matrix[0])

matrix = np.array(matrix)

diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1] - 1, -matrix.shape[0],-1))

columns = [matrix[:,i] for i in range(y)]
rows = [matrix[i,:] for i in range(x)]

count = 0

rows_string = []
columns_string = []
diags_string = []

for row in rows:
    string = ''.join(row)
    row_reversed = string[::-1]

    count += string.count("XMAS") + row_reversed.count("XMAS")


for col in columns:
    string = ''.join(col)
    col_reversed = string[::-1]

    count += string.count("XMAS") + col_reversed.count("XMAS")

for diag in diags:
    string = ''.join(diag)
    diag_reversed = string[::-1]

    count += string.count("XMAS") + diag_reversed.count("XMAS")

print(count)