


ex_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
""".strip()



def main(input:str):
    problems = parse_input(input)
    print(problems)
    
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


def parse_input(input:str):
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
            colOut.append(int(row[i]))
        colOut.append(out1[-1][i])
        out2.append(colOut)
    return out2

with open("./input.txt", "r") as f:
    real_input = f.read()

print(main(ex_input))
