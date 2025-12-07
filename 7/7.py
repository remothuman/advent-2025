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

def inputToList(input, toZeroes=False):
    rows = input.split("\n")
    rows_out = []
    for row in rows:
        if row[0] == "#":
            continue
        row_out = []
        for char in row:
            if toZeroes and char == ".":
                row_out.append(0)
            else:
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
    
    
    split_count = paint(rows, start_x, 1)
    
    print_screen(rows)
    print("split count", split_count)

    
    # split count to timelines
    # print(f"timelines guess: {2 ** split_count}")
    # no.... brain hurty
    
    

def print_screen(rows,*args):
    for row in rows:
        print(" ".join(row))
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
        if current_item == "^":
            if last_item not in {"^", "."}:
                # someone else has been here before
                return split_count
                # pass # thats ok cause its still a different timeline. but not doing this kills performance
            
            split_count += 1
            # print("split", start_x, current_y)
            rest = paint(rows, start_x + 1, current_y) + paint(rows, start_x - 1, current_y)
            split_count += rest
            return split_count
        # elif current_item == "|":
        #     pass
        elif current_item == ".":
            rows[current_y][start_x] = "1"
        else: 
            rows[current_y][start_x] = str(int(current_item) + 1)
    
        last_item = current_item
        # print_screen(rows, start_x, current_y)
        current_y += 1
        


def print_screen_2(rows):
    for row in rows:
        for item in row:
            if item == 0:
                item = "."
            print(f"{str(item):2}", end="")
        print()

def main2(input):
    rows = inputToList(input, True)
    start_x = None
    for col_i, col in enumerate(rows[0]):
        if col == "S":
            start_x = col_i
            break
    # print_screen_2(rows)
    rows[1][start_x] = 1
    
    for y in range(1, len(rows) - 1):
        row = rows[y]
        for x in range(len(row)):
            item = rows[y][x]
            if item == 0 or item == "^":
                continue
            
            item_below = rows[y+1][x]
            if item_below != "^":
                rows[y+1][x] += item
            else:
                rows[y+1][x+1] += item
                rows[y+1][x-1] += item
        
    print_screen_2(rows)
    
    total = 0
    for col in rows[-1]:
        total += col
    print("total", total)
    
    
    
    
    
    
    pass

main2(example_input)
main2(real_input)