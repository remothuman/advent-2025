
from reader import read_file_to_list

dial = 0

def turnDial(input, dir, amount):
    if dir == "L":
        return (input - amount) % 100
    elif dir == 'R':
        return (input + amount) % 100


print((99 + 10) % 100)
print((5 - 10) % 100)


input = read_file_to_list("./day1-input.txt")


dial = 50
zero_count = 0
for line in input:
    dir = line[0]
    amt = int(line[1:])
    if dial == 0:
        zero_count += 1
    
    dial = turnDial(dial, dir, amt)

print(zero_count)

