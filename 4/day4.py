ex_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()

def inputToList(input):
    rows = []
    for line in input.split("\n"):
        row = []
        for char in line:
            row.append(char)
        rows.append(row)
    return rows

def mainPtTwo(input):
    rows = inputToList(input)

    removed_count = 0
    while True:
        rows, valid_count = find_removable(rows)
        if valid_count == 0:
            break
        # remove the removable
        for row in rows:
            for i, item in enumerate(row):
                if item == "x":
                    row[i] = "."
        
        removed_count += valid_count

    for row in rows:
        print("".join(row)) 
    print(removed_count)
    


def find_removable(inputList):
    rows = inputList
    
    # determine adjacency
    # brute force cause why not and im undereducated on competitive programming

    valid_count = 0
    for row_i, row in enumerate(rows):
        for col_i, item in enumerate(row):
            if item == ".":
                continue

            # 3-8 adjacent coords
            adjacent_blocks = getAdjacentBlocks(row_i, col_i, rows)
            num_filled_adj = 0
            for pos_x, pos_y in adjacent_blocks:
                adj_block_value = rows[pos_x][pos_y]
                if adj_block_value == "@" or adj_block_value == "x":
                    num_filled_adj += 1
            
            if num_filled_adj < 4:
                rows[row_i][col_i] = "x"
                valid_count += 1

    # print(rows)
    # for row in rows:
    #     print("".join(row))

    # print(valid_count)
    return rows, valid_count
    

def getAdjacentBlocks(row_i, col_i, rows):
    max_col = len(rows) - 1
    max_row = len(rows[0]) - 1
    min_col = 0
    min_row = 0

    pos_1 = (row_i - 1, col_i - 1)
    pos_2 = (row_i - 1, col_i)
    pos_3 = (row_i - 1, col_i + 1)
    pos_4 = (row_i, col_i - 1)
    pos_5 = (row_i, col_i + 1)
    pos_6 = (row_i + 1, col_i - 1)
    pos_7 = (row_i + 1, col_i)
    pos_8 = (row_i + 1, col_i + 1)


    for pos in [pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8]:
        if pos[0] < min_row or pos[0] > max_row or pos[1] < min_col or pos[1] > max_col:
            continue
        yield pos
    


# print(list(getAdjacentBlocks(0, 0, inputToList(ex_input))))
# print(list(getAdjacentBlocks(3, 3, inputToList(ex_input))))

from input import real_input
# find_removable(real_input)
mainPtTwo(real_input)