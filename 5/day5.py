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
    
    def get_fresh_items_iter():
        for range_str in ranges:
            start, end = range_str.split("-")
            start, end = int(start), int(end)
            for i in range(start, end + 1):
                yield i
    def get_available_ids_iter():
        for available_id in available_ids:
            yield int(available_id)
    
    fresh_items = []
    fresh_items_iter = get_fresh_items_iter()
    available_ids_iter = get_available_ids_iter()
    
    current_fresh_item = next(fresh_items_iter)
    current_available_item = next(available_ids_iter)
    try: 
        while True:
            if current_fresh_item == current_available_item:
                fresh_items.append(current_fresh_item)
                print(f"found fresh item {current_available_item}")
                current_fresh_item = next(fresh_items_iter)
                # current_available_item = next(iter(available_ids))
            elif current_fresh_item < current_available_item:
                current_fresh_item = next(fresh_items_iter)
            else: # current_fresh_item > current_available_item
                current_available_item = next(available_ids_iter)
    except StopIteration:
        pass
    print(len(fresh_items))
    

main_2(real_input)

