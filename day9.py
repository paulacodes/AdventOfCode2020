def find_first_weakness(numbers):
	'''
	find_first_weakness finds the first number in a list that isn't equal to the 
	sum of the 25 numbers prior to it
	:param numbers: list of numbers
	'''
	starting_number = 0
	ending_number = 25
	for i in range(25, len(numbers)):
		current_num = numbers[i]
		current_array = numbers[starting_number:ending_number]
		current_sum = sum(current_array)
		found = False
		for j in current_array:
			if (current_num-j) in current_array:
				found = True
		if not found:
			return(current_num)
		starting_number += 1
		ending_number += 1

def find_contiguous_sum(numbers, number):
	'''
	find_contiguous_sum finds the first contiguous sublist of elements in a list
	whose elements sum up to a certain number, and returns the sum of the min
	and max values in that sublist
	:param numbers: list of numbers
	:param number: sum we're checking against
	'''
	current_array = numbers[0]
	start = 0
	i = 1
	# loop through numbers, changing starting and ending values of sublist 
	# based on whether the sum of the values between them are less, greater or 
	# equal to the sum we're looking for. If less, continue adding values. If 
	# greater, move starting value and reset count. Once equal, return the sum
	# of the min and max values.
	while i < len(numbers):
		if current_array == number:
			return(min(numbers[start:i]) + max(numbers[start:i]))
		if i <= len(numbers):
			current_array = current_array + numbers[i]
		if current_array > number:
			while current_array > number:
				current_array = current_array - numbers[start]
				start += 1
		i += 1


def part1():
	numbers = []
	with open('inputs/day9.txt') as f:
		for line in f:
			if line != "\n":
				numbers.append(int(line.strip("\n")))
	print(find_first_weakness(numbers))

def part2():
	numbers = []
	with open('inputs/day9.txt') as f:
		for line in f:
			if line != "\n":
				numbers.append(int(line.strip("\n")))
	number = find_first_weakness(numbers)
	print(find_contiguous_sum(numbers,number))

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()