import numpy as np

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

matrix = []

for line in lines:
    matrix.append([int(i) for i in line.strip()])

matrix = np.array(matrix)

rows, cols = np.where(matrix == 0)
zeros = []

for i,j in zip(rows,cols):
    zeros.append((i,j))


x = len(matrix)
y = len(matrix[0])

def traverse(i, j, curr, target, dest):
    if not (0 <= i < x and 0 <= j < y) or matrix[i][j] != curr:
        return 0
        
    if curr == target:
        dest.add((i,j))
        return 1
    
    return (traverse(i-1, j, curr + 1, target, dest) + 
            traverse(i+1, j, curr + 1, target, dest) + 
            traverse(i, j-1, curr + 1, target, dest) + 
            traverse(i, j+1, curr + 1, target, dest))
        
    

paths_total = 0
destinations_total = 0

for start in zeros:
    dest = set()
    paths = traverse(start[0], start[1], 0, 9, dest)
    destinations_total += len(dest)
    paths_total += paths

print(destinations_total, paths_total)
