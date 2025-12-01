
from reader import read_file_to_list

dial = 0
def turnDial(input, dir, amount):
    dial = input
    zero_passes = 0


    for i in range(amount):
        if dir == 'L':
            dial -= 1
            if dial == -1:
                dial = 99
        elif dir == 'R':
            dial += 1
            if dial == 100:
                dial = 0
        if dial == 0:
            zero_passes += 1
    # if we end on zero, and we've counted a pass landing on zero, we haven't passed it... wait the problem says any click that causes it to end on zero... the truth is just that we're already counting these clicks outside of this function so yeah
    if dial == 0 and zero_passes >= 1: 
        zero_passes -= 1

    return dial, zero_passes

print((99 + 10) % 100)
print((5 - 10) % 100)


print(turnDialO(50, 'R', 1000))
print(turnDialO(50, 'L', 68))


# input = read_file_to_list("./day1-ex.txt")
input = read_file_to_list("./day1-input.txt")


dial = 50
zero_count = 0
for line in input:
    dir = line[0]
    amt = int(line[1:])


    print(f'dial start: {dial}, doing: {line}', end="")
    
    dial, zero_passes = turnDialO(dial, dir, amt)
    zero_count += zero_passes
    # if dial == 0:
    #     zero_count += 1

    print(f"  |  dial end: {dial}, passes:{zero_passes}  new zero count: {zero_count}")

print(zero_count)


#5899