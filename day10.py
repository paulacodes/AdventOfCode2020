def part1():
	numbers = []
	with open('inputs/day10.txt') as f:
		for line in f:
			if line != "\n":
				numbers.append(int(line.strip("\n")))
	numbers.append(0)
	numbers.sort()
	numbers.append(numbers[-1]+3)
	one_jolt_differences = 0
	three_jolt_differences = 0
	for number in range(0, len(numbers)-1):
		if numbers[number+1] - numbers[number] == 1:
			one_jolt_differences += 1
		elif numbers[number+1] - numbers[number] == 3:
			three_jolt_differences += 1
	print(one_jolt_differences * three_jolt_differences)

def part2():
	numbers = []
	with open('inputs/day10.txt') as f:
		for line in f:
			if line != "\n":
				numbers.append(int(line.strip("\n")))
	numbers.append(0)
	numbers.sort()
	numbers.append(numbers[-1]+3)
	contiguous_sublists = []
	sublist = [numbers[0]]
	# find all contiguous sublists within the list
	for number in range(0, len(numbers)-1):
		if numbers[number+1] - numbers[number] == 1:
			sublist.append(numbers[number+1])
		else:
			contiguous_sublists.append(sublist)
			sublist = [numbers[number+1]]
	contiguous_sublists.append(sublist)	
	counts = {}
	for sublist in contiguous_sublists:
		if len(sublist) in counts: 
			counts[len(sublist)] += 1
		else:
			counts[len(sublist)] = 1
	result = 1
	# the following is based on several patterns in the input:
	#	- there are only jolts of 1 and 3
	#	- there are only contiguous sublists of 1,2,3,4 or 5 elements
	#	- there is only one way of using the elements in sublists of 1 or 2, 2 
	# ways of using the elements in sublists of 3, 4 ways in sublists of 4, and 
	# 7 ways in sublists of 5
	if 3 in counts:
		for num in range(counts[3]):
			result = result * 2
	if 4 in counts:
		for num in range(counts[4]):
			result = result * 4
	if 5 in counts:
		for num in range(counts[5]):
			result = result * 7
	print(result)


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()