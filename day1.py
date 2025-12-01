
from reader import read_file_to_list

dial = 0

def turnDial(input, dir, amount):
    out = 0 
    if dir == "L":
        out = (input - amount)
    elif dir == 'R':
        out = (input + amount)
    
    
    if out < 0 or out > 99:
        return out % 100, 1
    return out, 0
    # we expect dir to be <100 so only at max one click


print((99 + 10) % 100)
print((5 - 10) % 100)


input = read_file_to_list("./day1-input.txt")


dial = 50
zero_count = 0
for line in input:
    dir = line[0]
    amt = int(line[1:])
    
    dial, clicks = turnDial(dial, dir, amt)
    zero_count += clicks

    if dial == 0:
        zero_count += 1

print(zero_count)

