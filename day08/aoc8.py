from collections import defaultdict
from itertools import combinations

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

matrix = []

for line in lines:
    matrix.append([c for c in line.strip()])

chars = defaultdict(list)
antinodes = set()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        el = matrix[i][j]
        if el != ".":
            chars[el].append((i, j))

total = 0

for c, f in chars.items():
    for val1, val2 in combinations(f, 2):
        i_diff = abs(val1[0] - val2[0])
        j_diff = abs(val1[1] - val2[1])

        if val1[0] < val2[0] and val1[1] < val2[1]:
            new_i1 = val1[0] - i_diff
            new_j1 = val1[1] - j_diff

            new_i2 = val2[0] + i_diff
            new_j2 = val2[1] + j_diff

        elif val1[0] >= val2[0] and val1[1] < val2[1]:
            new_i1 = val1[0] + i_diff
            new_j1 = val1[1] - j_diff

            new_i2 = val2[0] - i_diff
            new_j2 = val2[1] + j_diff

        elif val1[0] < val2[0] and val1[1] >= val2[1]:
            new_i1 = val1[0] - i_diff
            new_j1 = val1[1] + j_diff

            new_i2 = val2[0] + i_diff
            new_j2 = val2[1] - j_diff

        elif val1[0] >= val2[0] and val1[1] >= val2[1]:
            new_i1 = val1[0] + i_diff
            new_j1 = val1[1] + j_diff

            new_i2 = val2[0] - i_diff
            new_j2 = val2[1] - j_diff

        if (new_i1 >= 0 and new_i1 < len(matrix)) and (
            new_j1 >= 0 and new_j1 < len(matrix[0])
        ):
            antinodes.add((new_i1, new_j1))

        if (new_i2 >= 0 and new_i2 < len(matrix)) and (
            new_j2 >= 0 and new_j2 < len(matrix[0])
        ):
            antinodes.add((new_i2, new_j2))

print(len(antinodes))
