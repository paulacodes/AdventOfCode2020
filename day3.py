#Part 1
import numpy
from numpy import prod

def part1():
	matrix = []
	with open('inputs/day3.txt') as f:
		for line in f:
			row = []
			row.extend(line.strip('\n'))
			matrix.append(row)
	f.close()
	current_row = 0
	current_col = 0
	trees = 0
	while current_row + 1 < len(matrix):
		if current_col + 3 < len(row):
			current_row += 1
			current_col += 3
			if matrix[current_row][current_col] == "#":
				trees += 1
		else:
			current_col = 3 -(len(row) - current_col)
			current_row += 1
			if matrix[current_row][current_col] == "#":
				trees += 1
	print("Trees encountered:", str(trees))

def part2():
	matrix = []
	with open('inputs/day3.txt') as f:
		for line in f:
			row = []
			row.extend(line.strip('\n'))
			matrix.append(row)
	f.close()
	slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
	all_trees = []
	for slope in slopes:
		right = slope[0]
		down = slope[1]
		current_row = 0
		current_col = 0
		trees = 0
		while current_row + down < len(matrix):
			if current_col + right < len(row):
				current_row += down
				current_col += right
				if matrix[current_row][current_col] == "#":
					trees += 1
			else:
				current_col = right -(len(row) - current_col)
				current_row += down
				if matrix[current_row][current_col] == "#":
					trees += 1
		all_trees.append(trees)
	print("Trees encountered, multiplied:", str(numpy.prod(all_trees)))


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()