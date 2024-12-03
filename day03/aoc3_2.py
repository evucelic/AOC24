import re

input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.read()

sum = 0

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
enabled = True

string = lines.strip()
while string:
    if enabled:
        before, _, string = string.partition(r"don't()")

        for match in pattern.findall(before):
            l, r = int(match[0]), int(match[1])
            sum += l*r
        
        enabled = False
    
    else:
        before, _ , string = string.partition(r"do()")
        enabled = True

print(sum)
