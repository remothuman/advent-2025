

example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
real_input = "516015-668918,222165343-222281089,711089-830332,513438518-513569318,4-14,4375067701-4375204460,1490-3407,19488-40334,29275041-29310580,4082818-4162127,12919832-13067769,296-660,6595561-6725149,47-126,5426-11501,136030-293489,170-291,100883-121518,333790-431800,897713-983844,22-41,42727-76056,439729-495565,43918886-44100815,725-1388,9898963615-9899009366,91866251-91958073,36242515-36310763"


def main(input):
    ranges = input.split(",")
    invalid_count = 0
    invalid_sum = 0
    for range_str in ranges:
        start, end = range_str.split("-")
        start, end = int(start), int(end)
        for i in range(start, end + 1):
            if is_invalid(i):
                invalid_count += 1
                invalid_sum += i
                # print(i)
    return invalid_sum, invalid_count
        

def is_invalid(num):
    # made only of some sequence of digits repeated twice
    digits = str(num)

    for pattern_length in range(1, len(digits)):
        patternToCheck = digits[0:pattern_length]
        # print("--", patternToCheck, (patternToCheck * 2))

        # if digits == patternToCheck * 2:
        #     return True

        if len(digits) % len(patternToCheck) != 0:
            continue


        # check if word is made of pattern repeated
        for s in range(0, len(digits), len(patternToCheck)):
            subsection_matches = digits[s:s+len(patternToCheck)] == patternToCheck 
            if not subsection_matches:
                break
        else: # executes if for loop didn't break
            return True
    return False


# print(check_validity(1122))
# print(check_validity(55))
# print(check_validity(1234))
# print(check_validity(1188511885))

print(main(example_input))
print(main(real_input))