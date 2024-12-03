import re

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    string = line.strip()

    m = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", string)

    for pair in m:
        l, r = int(pair[0]), int(pair[1])
        prod = l*r
        sum += prod

print(sum)