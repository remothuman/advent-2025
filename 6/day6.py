


ex_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip("\n")



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
    
    print(out1)
    
    # convert into column array
    out2 = []
    for i in range(len(out1[0])):
        colOut = []
        for row in out1[:-1]:
            colOut.append(int(row[i]) if intify else row[i])
        colOut.append(out1[-1][i])
        out2.append(colOut)
    return out2


def parse_input_part2_bad(input:str):
    # convert into 2D array
    rows = input.split("\n")
    print(input)
    digits_per_row = len(rows[0])
    
    # damnit this has been the wrong strategy all along
    out_1_rows = []
    for row in rows:
        next_number = ""
        in_gap = True
        row_out = []
        for digit_i in range(digits_per_row -1 , -1, -1):
            current_char = row[digit_i]
            print(f"[{digit_i}]{current_char}", end="")
            if not in_gap:
                if current_char == " ":
                    row_out.insert(0, next_number)
                    next_number = ""
                    in_gap = True
                else:
                    next_number = f"{current_char}{next_number}"
            else: # in gap
                if current_char != " ":
                    in_gap = False
                next_number = f"{current_char}{next_number}"
        # do last num
        row_out.insert(0, next_number)
        out_1_rows.append(row_out)
        print("")
    
    for r in out_1_rows:
        print(r)
        
    out_2_problems = []
    num_problems = len(out_1_rows[0])
    for problem_i in range(num_problems):
        for row in out_1_rows[:-1]: # exclude op;erator row
            pass

# def parse_input_part1112(input:str):
#     """
#     Plan:
#     1. break into each problem
#     2. continue on
#     """
#     problems_unprocessed = parse_input_part2(input)
    
def parse_input_part2(input:str):
    rows = input.split("\n")
    num_chars_per_row = len(rows[0])
    
    num_rows = len(rows)
    
    problems = []
    current_problem = []
    current_problem_operator = None
    for char_x in range(num_chars_per_row):
        number = ""
        for row in rows[:-1]:
            number += row[char_x]
        if rows[-1][char_x] != " ":
            current_problem_operator = rows[-1][char_x]
            
        if number == " "*(num_rows-1):
            # this is start of new problem
            current_problem.append(current_problem_operator)
            problems.append(current_problem)
            current_problem = []
            current_problem_operator = None
        else:
            # continue on to next char_x aka number
            current_problem.append(number)
    # for last one
    current_problem.append(current_problem_operator)
    problems.append(current_problem)
            
    # print(problems)
    
    # strip out whitespace and intify
    out = []
    for problem in problems:
        out_problem = []
        for number in problem[:-1]:
            out_problem.append(int(number.strip()))
        out_problem.append(problem[-1])
        out.append(out_problem)
    
    return out
    
            
def convert_problem_to_correct_format(problem:list[str]):
    longest_digit_length = max(len(str(number)) for number in problem)
    
    out = []
    
    for digit_col in range(longest_digit_length, 0, -1):
        built_number = ""
        for number in problem[:-1]: # exclude the operator row
            if len(str(number)) >= digit_col:
                built_number += str(number[digit_col-1])
            else:
                built_number += ""
        out.append(built_number)
        
    out.append(problem[-1]) # add the operator row
    return out


with open("./input.txt", "r") as f:
    real_input = f.read().strip("\n")
with open("./input_trunc.txt", "r") as f:
    trunc_input = f.read().strip("\n")

# print(main(ex_input, part2=True))
# print(main(real_input))

print(parse_input_part2(ex_input))
# for r in parse_input_part2(trunc_input):
#     print(r)
    
print(main(ex_input, part2=True))
print(main(real_input, part2=True))


