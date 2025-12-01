
from reader import read_file_to_list

dial = 0

def turnDialO(input, dir, amount):
    if dir == "L":
        out = (input - amount)
    elif dir == 'R':
        out = (input + amount)
    

    zero_clicks = 0

    if out == 0:
        zero_clicks += 1
    
    while out < 0:
        out += 100
        zero_clicks += 1
    while out > 99:
        out -= 100
        zero_clicks += 1

    # if out == 0:
    #     zero_clicks += 1
    # # if we started on zero and -> -1 we may double count
    # if (input == 0 and zero_clicks >= 1 and dir=="L") or (input==99 and zero_clicks >=1 and dir=="R"):
    #     zero_clicks -= 1
    
    return out, zero_clicks


def turnDialAlt(input, dir, amount):
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

    return dial, zero_passes


input = read_file_to_list("./day1-ex.txt")
# input = read_file_to_list("./day1-input.txt")


def main(turnDial):
    dial = 50
    zero_count = 0
    for line in input:
        dir = line[0]
        amt = int(line[1:])


        print(f'dial start: {dial}, doing: {line}', end="")
        
        dial, zero_passes = turnDial(dial, dir, amt)
        zero_count += zero_passes

        print(f"  |  dial end: {dial}, passes:{zero_passes}  new zero count: {zero_count}")
    return zero_count

print('original', main(turnDialO))
# print('alt', main(turnDialAlt))


#5899