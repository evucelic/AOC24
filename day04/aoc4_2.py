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

count = 0

def x_check(matrix, i, j):
     
    if i <= 0 or j <= 0 or i >= len(matrix[0])-1 or j >= len(matrix)-1:
        return False
     
    top_left = matrix[i-1][j-1]
    top_right = matrix[i-1][j+1]
    bot_left = matrix[i+1][j-1]
    bot_right = matrix[i+1][j+1]

    if top_left == 'M' and top_right == 'M' and bot_left == 'S' and bot_right == 'S':
        return True

    elif top_left == 'S' and top_right == 'S' and bot_left == 'M' and bot_right == 'M':
        return True

    elif top_left == 'M' and top_right == 'S' and bot_left == 'M' and bot_right == 'S':
        return True

    elif top_left == 'S' and top_right == 'M' and bot_left == 'S' and bot_right == 'M':
        return True

    return False


for i, row in enumerate(matrix):
    for j, letter in enumerate(row):
        if letter == "A":
            count += x_check(matrix, i, j)

print(count)
            
