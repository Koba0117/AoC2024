import re

input_path = "./input.txt"
mul_pattern = r"mul\(\d+,\d+\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
answer = 0
data = ""

with open(input_path) as file:
    for line in file:
        data += line

    data = " ".join(part.split("don't()")[0] for part in data.split("do()"))
    mul_matches = re.findall(mul_pattern, data)
    for muls in mul_matches:
        nums = re.findall(r"\d+", muls)
        answer += int(nums[0]) * int(nums[1])

print(answer)
