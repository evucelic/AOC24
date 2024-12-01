input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

L = []
R = []

for line in lines:
    l, r = line.strip().split()
    L.append(int(l))
    R.append(int(r))

L = sorted(L)
R = sorted(R)

sum = 0

for idx, i in enumerate(L):
    distance = abs(i - R[idx])
    sum+=distance

print(sum)