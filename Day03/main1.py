import re

input_path = "./input.txt"
mul_pattern = r"mul\(\d+,\d+\)"
answer = 0

with open(input_path) as file:
    for line in file:
        mul_matches = re.findall(mul_pattern, line)
        for muls in mul_matches:
            nums = re.findall(r"\d+", muls)
            answer += int(nums[0]) * int(nums[1])

print(answer)
