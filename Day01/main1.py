input_path = "./input.txt"
list1 = []
list2 = []
answer = 0

with open(input_path) as file:
    for line in file:
        list1.append(int(line[0:5]))
        list2.append(int(line[8:13]))

list1.sort()
list2.sort()

for i, loc_id in enumerate(list1):
    answer += abs(loc_id - list2[i])

print(answer)
