def multiply_two_numbers_that_sum_to_value(numbers, value):
	"""
	multiply_two_numbers_that_sum_to_value finds the two numbers in a list that 
	sum to a certain value and returns the multiplied values
	:param numbers: list of numbers
	:param value: the value that the two numbers shuld sum up to
	"""
	subset = set()
	for i in range(0, len(numbers)):
		sub = value - numbers[i]
		if sub in subset:
			return(sub*numbers[i])
			break
		subset.add(numbers[i])
	return(0)

def multiply_three_numbers_that_sum_to_value(numbers, value):
	"""
	multiply_three_numbers_that_sum_to_value finds the three numbers in a list 
	that sum to a certain value and returns the multiplied values
	:param numbers: list of numbers
	:param value: the value that the three numbers should sum up to
	"""
	numbers.sort()
	for i in range(0, len(numbers)-2):
		l = i + 1
		r = len(numbers) - 1
		while (l<r):
			current_sum = numbers[i]+numbers[l]+numbers[r]
			if current_sum == 2020:
				return(numbers[i]*numbers[l]*numbers[r])
				break
			elif current_sum < 2020:
				l += 1
			else:
				r -= 1
	return(0)

def part1():
	numbers = []
	with open('inputs/day1.txt') as f:
	    for line in f:
	        numbers.append(int(line.strip('\n')))
	f.close()
	result = multiply_two_numbers_that_sum_to_value(numbers, 2020)
	print("Result:", str(result))


def part2():
	numbers = []
	with open('inputs/day1.txt') as f:
	    for line in f:
	        numbers.append(int(line.strip('\n')))
	f.close()
	result = multiply_three_numbers_that_sum_to_value(numbers, 2020)
	print("Result:", str(result))
	

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()