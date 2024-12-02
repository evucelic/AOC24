input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    line = line.strip().split()

    line = [int(el) for el in line]

    safe = False

    increasing = all(i < j for i, j in zip(line, line[1:]))
    decreasing = all(i > j for i, j in zip(line, line[1:]))

    if increasing:
        safe = all(j-i >=1 and j-i <=3 for i,j in zip(line,line[1:]))

    elif decreasing:
        safe = all(i-j >=1 and i-j <=3 for i,j in zip(line,line[1:]))

    
    if safe:
        sum += 1

print(sum)