


ex_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
""".strip()



def main(input:str, part2=False):
    if not part2:
        problems = parse_input_part1(input)
    else:
        problems = parse_input_part2(input)
    
    total = 0
    for problem in problems:
        operator = problem.pop()
        if operator == "+":
            result = sum(problem)
        elif operator == "*":
            result = 1
            for num in problem:
                result *= num
        total += result
    return total


def parse_input_part1(input:str, intify=True):
    # convert into 2D array
    rows = input.split("\n")
    out1 = []
    for row in rows:
        rowOut = []
        nums = row.split(" ")
        for num in nums:
            num = num.strip()
            if num == "":
                continue
            rowOut.append(num)
        out1.append(rowOut)
    
    # print(out1)
    
    # convert into column array
    out2 = []
    for i in range(len(out1[0])):
        colOut = []
        for row in out1[:-1]:
            colOut.append(int(row[i]) if intify else row[i])
        colOut.append(out1[-1][i])
        out2.append(colOut)
    return out2


def parse_input_part2(input:str):
    numbers_1 = parse_input_part1(input, intify=False)
    
    out1 = []
    for problem in numbers_1:
        out1.append(convert_problem_to_correct_format(problem))
        print(out1[-1])
        
        
            
def convert_problem_to_correct_format(problem:list[str]):
    longest_digit_length = max(len(str(number)) for number in problem)
    
    out = []
    
    for i in range(longest_digit_length, 0, -1):
        built_number = ""
        for number in problem[:-1]:
            if len(str(number)) >= i:
                built_number += str(number[i-1])
            else:
                built_number += ""
        out.append(built_number)
        
    out.append(problem[-1])
    return out


with open("./input.txt", "r") as f:
    real_input = f.read().strip()
with open("./input_trunc.txt", "r") as f:
    trunc_input = f.read().strip()

print(main(ex_input, part2=True))
# print(main(real_input))

# print(parse_input_part2(trunc_input))

