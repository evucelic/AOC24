from collections import defaultdict

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

ordering, updates = defaultdict(list), []

ordering2 = []

for i, line in enumerate(lines):
    if line.strip() != "":
        l,r = line.strip().split("|")
        ordering[int(l)].append(int(r))
        ordering2.append((int(l),int(r)))
    else:
        updates = lines[i+1:]
        break

updates = [u.strip().split(",") for u in updates]

sum = 0

for update in updates:
    hierarchy = defaultdict(int)
    ll = [int(u) for u in update]
    for u in update:
        for j in update:
            if j == u:
                continue
            if int(j) in ordering[int(u)]:
                hierarchy[int(u)] -= 1
            else:
                hierarchy[int(u)] = 0
    increasing = all(i < j for i, j in zip(list(hierarchy.values()), list(hierarchy.values())[1:]))

    if not increasing:
        d = defaultdict()
        for g in ll:
            d[g] = 0
        for l,r in ordering2:
            if l in ll and r in ll:
                d[l] += 1 # inkrement broja elemenata nakon lijevog
        
        for g in ll:
            if d[g] == len(ll)//2: # ako je broj elemenata nakon lijevog == pola elemenata s jedne strane to mora biti sredina
                sum+= g
                break

print(sum)
