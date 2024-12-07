from collections import defaultdict

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

val = []

for line in lines:
    l, r = line.strip().split(":")
    numbers = [int(x) for x in r.strip().split()]
    numbers.insert(0,int(l))
    val.append(numbers)


def check(target, current, calibrations):
    if not calibrations:
        return target == current
    
    if current > target:
        return False
    
    return check(target, current * calibrations[0], calibrations[1:]) or check(target, current + calibrations[0], calibrations[1:])

total = 0

for row in val:
    if check(row[0], row[1], row[2:]):
        total += row[0]

print(total)