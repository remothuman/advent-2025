from input import i
"""
Problem:
The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce. In the above example:

    In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    In 818181911112111, the largest joltage you can produce is 92.


"""
ex_input = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()


def main(input):
    sum = 0
    for line in input.split("\n"):
        sum += find_max_joltage(line)
    return sum

def find_max_joltage(line, onDigits=12):
    print(line, end="\n")
    digits = []

    start = 0
    left = -1 * (onDigits - 1)
    for i in range(onDigits):
        if left == 0:
            lineToCheck = line[start:]
        else:
            lineToCheck = line[start:left]
        max_digit, max_digit_index = find_max_digit(lineToCheck)

        digits.append(str(max_digit))

        max_digit_index += start

        print(lineToCheck, digits, max_digit, max_digit_index, start, left)
        start = max_digit_index + 1
        left += 1

    print(int("".join(digits)))
    print("\n")
    return int("".join(digits))

def find_max_digit(line):
    max_digit = -1
    max_digit_index = -1
    for i, digit_char in enumerate(line):
        digit = int(digit_char)
        if digit > max_digit:
            max_digit = digit
            max_digit_index = i
    return max_digit, max_digit_index



# print(main(i))

# print(find_max_joltage("9987654321111111", 12))

print(find_max_joltage("818181911112111", 12))
print(main(ex_input))

print(main(i))