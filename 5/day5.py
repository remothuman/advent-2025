ex_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()
with open("./vibe/day5_input.txt", "r") as f:
    real_input = f.read()

def main_1(input):
    ranges, available_ids = input.split("\n\n")
    ranges = ranges.split("\n")
    available_ids = available_ids.split("\n")
    
    available_set = set(map(int, available_ids))
    fresh_set = set()
    num_fresh = 0
    
    print("built set")
    # print(available_set)
    for range_str in ranges:
        start, end = range_str.split("-")
        start, end = int(start), int(end)
        for i in range(start, end + 1):
            if i in available_set:
                fresh_set.add(i)
                num_fresh += 1
        print(f"checked range {range_str}, total is {num_fresh} fresh")
    
    print(num_fresh)
    # ok this version not fast enough
        
    
def main_2(input):
    ranges, available_ids = input.split("\n\n")
    ranges = ranges.split("\n")
    available_ids = available_ids.split("\n")
    
    def get_range(range_index):
        start, end = ranges[range_index].split("-")
        return range(int(start), int(end) + 1)
    
    current_range_index = 0
    current_range = get_range(current_range_index)
    current_available_index = 0
    while True:
        available_item = available_ids[current_available_index]
        current_fresh_item = ranges[current_range_index]
        next_fresh_item = current_range.next()
        
    
    

main_2(ex_input)

