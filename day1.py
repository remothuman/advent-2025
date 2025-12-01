
from reader import read_file_to_list

dial = 0

def turnDial(input, dir, amount):
    out = 0 
    if dir == "L":
        out = (input - amount)
    elif dir == 'R':
        out = (input + amount)
    
    
    clicks = 0
    while out < 0:
        out += 100
        clicks += 1
    while out > 99:
        out -= 100
        clicks += 1
    return out, clicks


print((99 + 10) % 100)
print((5 - 10) % 100)


print(turnDial(50, 'R', 1000))
print(turnDial(50, 'L', 68))


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

