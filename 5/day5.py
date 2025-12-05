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
        sorted_ranges = sorted(ranges, key=lambda x: int(x.split("-")[0]))
        for range_str in sorted_ranges:
            start, end = range_str.split("-")
            start, end = int(start), int(end)
            for i in range(start, end + 1):
                yield i
    def get_available_ids_iter():
        sorted_available_ids = sorted(available_ids, key=lambda x: int(x))
        for available_id in sorted_available_ids:
            yield int(available_id)
    
    fresh_items = []
    fresh_items_iter = get_fresh_items_iter()
    available_ids_iter = get_available_ids_iter()
    
    current_fresh_item = next(fresh_items_iter)
    current_available_item = next(available_ids_iter)
    try: 
        print(f"starting with {current_fresh_item} and {current_available_item}")
        while True:
            if current_fresh_item == current_available_item:
                fresh_items.append(current_fresh_item)
                print(f"found fresh item {current_available_item}")
                current_fresh_item = next(fresh_items_iter)
                # current_available_item = next(iter(available_ids))
            elif current_fresh_item < current_available_item:
                # then its not fresh
                current_fresh_item = next(fresh_items_iter)
            else: # current_fresh_item > current_available_item
                # then we have to move the available item forward
                # should move it forward by more than one
                current_available_item = next(available_ids_iter)
    except StopIteration:
        pass
    print(len(fresh_items))
    
    # still too slow. maybe need binary type search


def main_3(input):
    ranges_strs, available_ids_strs = input.split("\n\n")
    ranges_strs = ranges_strs.split("\n")
    available_ids_strs = available_ids_strs.split("\n")
    
    def get_ranges_iter():
        sorted_ranges = sorted(ranges_strs, key=lambda x: int(x.split("-")[0]))
        for range_str in sorted_ranges:
            start, end = range_str.split("-")
            start, end = int(start), int(end)
            yield (start, end)
    def get_available_ids_iter():
        sorted_available_ids = sorted(available_ids_strs, key=lambda x: int(x))
        for available_id in sorted_available_ids:
            yield int(available_id)
    
    fresh_items_output = []
    
    ranges = get_ranges_iter()
    available_ids = get_available_ids_iter()
    
    range_start, range_end = next(ranges)
    available_id = next(available_ids)
    
    
    try:
        while True:
            is_in_range = available_id >= range_start and available_id <= range_end
            if is_in_range:
                fresh_items_output.append(available_id)
                available_id = next(available_ids)
                continue
            elif available_id < range_start:
                available_id = next(available_ids)
                # this one not fresh
                continue
            elif available_id > range_end:
                range_start, range_end = next(ranges)
            else:
                break
    except StopIteration:
        pass
    print(len(fresh_items_output))


def main_part_2(input):
    # ?? I see we don't want to iterate over it, just count it
    # I would add it for each range, but they can overlap...
    
    ranges_strs, _ = input.split("\n\n")
    ranges_strs = ranges_strs.split("\n")
    def get_ranges_iter():
        sorted_ranges = sorted(ranges_strs, key=lambda x: int(x.split("-")[0]))
        for range_str in sorted_ranges:
            start, end = range_str.split("-")
            start, end = int(start), int(end)
            yield (start, end)
    
    
    ranges = get_ranges_iter()
    total_fresh = 0
    
    last_range_start, last_range_end = -1, -1
    for range_start, range_end in ranges:
        _old_total_fresh = total_fresh
        if range_start > last_range_end:
            total_fresh += range_end - range_start + 1
        elif range_end < last_range_end:
            # its within the last range
            pass
        else:
            total_fresh += range_end - last_range_end
        last_range_start, last_range_end = range_start, range_end
        
        print(range_start, range_end, f"+{total_fresh - _old_total_fresh}", f"({total_fresh})")
    print(total_fresh)
    


main_part_2(real_input)
main_part_2(ex_input)

