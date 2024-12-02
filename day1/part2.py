import time
start_time = time.time()

with open('input', 'r') as f:
    lines = f.readlines()
first_list = list()
second_list = dict()
for line in lines:
    num_split = line.split()
    first_list.append(num_split[0])
    if second_list.get(num_split[1]) is not None:
        second_list[num_split[1]] += 1
    else:
        second_list[num_split[1]] = 1

first_list.sort()

sum = 0
for i in range(len(first_list)):
    if second_list.get(first_list[i]):
        sum += int(first_list[i]) * second_list[first_list[i]]
print(sum)

execution_time = time.time() - start_time
print("Execution time:", execution_time, "seconds")
