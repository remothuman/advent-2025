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

def find_max_joltage(line):
    print(line, end="--")
    # find first digit (largest digit)
    max_digit = -1
    max_digit_index = -1
    for i, digit_char in enumerate(line[0:-1]):
        digit = int(digit_char)
        if digit > max_digit:
            max_digit = digit
            max_digit_index = i

    # find second digit (largest digit after the first one)
    second_max_digit = -1
    second_max_digit_index = -1
    for i, digit_char in enumerate(line[max_digit_index+1:]):
        digit = int(digit_char)
        if digit > second_max_digit:
            second_max_digit = digit
            second_max_digit_index = max_digit_index + 1 + i

    out = f"{line[max_digit_index]}{line[second_max_digit_index]}"
    print(out)
    return int(out)


print(main(i))