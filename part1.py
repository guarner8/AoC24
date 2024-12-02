with open('input', 'r') as f:
    lines = f.readlines()
    first_list = list()
    second_list = list()
    for line in lines:
    	num_split = line.split()
    	first_list.append(int(num_split[0]))
    	second_list.append(int(num_split[1]))

first_list.sort()
second_list.sort()

sum = 0
for i in range(len(first_list)):
	sum += abs(first_list[i] - second_list[i])
print(sum)