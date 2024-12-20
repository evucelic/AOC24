input_path = "input.txt"

input = open(input_path,"r").read().strip()

blinks = 25

input_list = input.split()

while blinks > 0:
    new_list = []
    for el in input_list:
        if int(el) == 0:
            new_list.append("1")
        elif len(el) % 2 == 0:
            n = len(el) // 2
            new_el1 = el[:n]
            new_el2 = el[n:]
            new_list.append(str(int(new_el1)))
            new_list.append(str(int(new_el2)))
        else:
            new_list.append(f"{int(el)*2024}")
    blinks -= 1
    input_list = new_list

print(len(new_list))


