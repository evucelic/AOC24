input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    line = line.strip().split()

    line = [int(el) for el in line]

    safe = False

    iterations = [line[:i] + line[i+1:] for i in range(len(line))]

    iterations.append(line)

    for iteration in iterations:

        increasing = all(i < j for i, j in zip(iteration, iteration[1:]))
        decreasing = all(i > j for i, j in zip(iteration, iteration[1:]))

        if increasing:
            safe = all(j-i >=1 and j-i <=3 for i,j in zip(iteration,iteration[1:]))

        elif decreasing:
            safe = all(i-j >=1 and i-j <=3 for i,j in zip(iteration,iteration[1:]))

        
        if safe:
            sum += 1
            break

print(sum)