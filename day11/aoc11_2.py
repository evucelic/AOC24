from collections import Counter

input_path = "input.txt"

input = open(input_path,"r").read().strip()

blinks = 75

input_list = Counter(input.split())

while blinks > 0:
    new_list = Counter()
    for el,count in input_list.items():
        if int(el) == 0:
            new_list["1"] += count
        elif len(el) % 2 == 0:
            n = len(el) // 2
            new_el1 = el[:n]
            new_el2 = el[n:]
            new_list[str(int(new_el1))] += count
            new_list[str(int(new_el2))] += count
        else:
            new_list[str(int(el)*2024)] += count
    
    blinks -= 1
    input_list = new_list

print(sum(new_list.values()))