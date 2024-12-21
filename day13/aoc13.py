input_path = "input.txt"

input = open(input_path,"r").read().split("\n")

t = []
cond = True

while cond:
    try:
        temp_idx = input.index("")
    except:
        cond = False

    t.append(input[:temp_idx])
    input = input[temp_idx+1:]

total = 0

for el in t:
    x1 = int(el[0].split(":")[1].strip().split(",")[0].strip().split("+")[1].strip())
    y1 = int(el[0].split(":")[1].strip().split(",")[1].strip().split("+")[1].strip())

    x2 = int(el[1].split(":")[1].strip().split(",")[0].strip().split("+")[1].strip())
    y2 = int(el[1].split(":")[1].strip().split(",")[1].strip().split("+")[1].strip())

    px = int(el[2].split(":")[1].strip().split(",")[0].strip().split("=")[1].strip())
    py = int(el[2].split(":")[1].strip().split(",")[1].strip().split("=")[1].strip())

    b = (px*y1 - x1*py) / (x2*y1 - x1*y2)
    if b == int(b) and 0 <= b <= 100:
        b = int(b)
        a = (px - x2*b) / x1
        if (a == int(a) and 0 <= a <= 100 and 
            a*y1 + b*y2 == py):
            a = int(a)
            total += 3*a + b
    

print(total)