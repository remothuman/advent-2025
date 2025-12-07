example_input = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()

with open("in.txt", "r") as file:
    real_input = file.read().strip("\n")

def inputToList(input):
    rows = input.split("\n")
    rows_out = []
    for row in rows:
        if row[0] == "#":
            continue
        row_out = []
        for char in row:
            row_out.append(char)
        rows_out.append(row_out)
    return rows_out

def main(input):
    rows = inputToList(input)
    
    split_count = 0
    
    start_x = None
    for col_i, col in enumerate(rows[0]):
        if col == "S":
            start_x = col_i
            break
    
    
    res = paint(rows, start_x, 1)
    
    print_screen(rows)
    print("done", res)
    return res

def print_screen(rows,*args):
    for row in rows:
        print("".join(row))
    print(*args)
    
    print("--------------------------------")

def paint(rows, start_x, start_y):
    # current_x = start_x
    current_y = start_y
    split_count = 0
    last_item = None
    while True:
        if current_y == len(rows):
            return split_count
        
        
        current_item = rows[current_y][start_x]
        if current_item == ".":
            rows[current_y][start_x] = "|"
        elif current_item == "^":
            if last_item == "|":
                # someone else has been here before
                return split_count
            
            split_count += 1
            print("split", start_x, current_y)
            rest = paint(rows, start_x + 1, current_y) + paint(rows, start_x - 1, current_y)
            split_count += rest
            return split_count
        elif current_item == "|":
            pass
    
        last_item = current_item
        # print_screen(rows, start_x, current_y)
        current_y += 1
        


main(real_input)
    