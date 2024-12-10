input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

input = open(input_path, "r").read()

full = []

id = 0

for i,c in enumerate(input):
    if i%2 == 0:
        full.extend(int(c) * [str(id)])
        id += 1
    else:
        if int(c) != 0:
            full.extend(int(c) * ['.'])
    
first_free = full.index('.')

for i in reversed(range(0, len(full))):
    if full[i] != ".":
        full[first_free] = full[i]
        full[i] = '.'
        first_free = full.index('.')
        if i - first_free <= 0:
            break

checksum = 0

for n,c in enumerate(full):
    if c == ".":
        break
    checksum += n*int(c)

print(checksum)