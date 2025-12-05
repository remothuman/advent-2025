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

def main(input):
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
        print(f"checked range {range_str}, found {num_fresh} fresh")
    
    print(num_fresh)

main(real_input)
# ok this version not fast enough