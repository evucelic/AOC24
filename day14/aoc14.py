import numpy as np

input_path = "input.txt"

input = open(input_path,"r").read().split("\n")

n = 101
m = 103
seconds = 100

matrix = np.zeros((n,m))

for el in input:
    x,y = el.split()[0].split("=")[1].split(",")
    vx, vy = el.split()[1].split("=")[1].split(",")
    x,y,vx,vy = int(x), int(y), int(vx), int(vy)

    for _ in range(seconds):
        x = (x + vx) % n
        y = (y + vy) % m  

    matrix[x][y] += 1

matrix = np.transpose(matrix)

mid_n = n // 2
mid_m = m // 2

q1 = matrix[:mid_m, :mid_n].sum()
q2 = matrix[:mid_m, mid_n+1:].sum()
q3 = matrix[mid_m+1:, :mid_n].sum()
q4 = matrix[mid_m+1:, mid_n+1:].sum()


print(int(q1*q2*q3*q4))