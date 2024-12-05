from collections import defaultdict

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

ordering, updates = defaultdict(list), []

for i, line in enumerate(lines):
    if line.strip() != "":
        l,r = line.strip().split("|")
        ordering[int(l)].append(int(r))
    else:
        updates = lines[i+1:]
        break

updates = [u.strip().split(",") for u in updates]

sum = 0

for update in updates:
    hierarchy = defaultdict(int)
    for u in update:
        for j in update:
            if j == u:
                continue
            if int(j) in ordering[int(u)]:
                hierarchy[int(u)] -= 1
            else:
                hierarchy[int(u)] = 0
    increasing = all(i < j for i, j in zip(list(hierarchy.values()), list(hierarchy.values())[1:]))
    if increasing :
        sum += int(update[(len(update) -1)//2])

print(sum)