import math
import itertools
import copy
def part1():
	rows = []
	empty_rows = []
	num_slices = 0
	data = []
	cycles = 6
	with open('inputs/day17.txt') as f:
		for line in f:
			row = list(line.strip("\n"))
			data.append(row)
	num_slices = cycles * 2 + 1
	for row in data:
		for cycle in range(cycles):
			row.append(".")
			row.insert(0,".")
		rows.append(row)
	for cycle in range(cycles):
		rows.insert(0,["."]*len(row))
		rows.append(["."]*len(row))
	for i in range(20):
		empty_rows.append(['.']*len(row))
	slices = []
	for i in range(num_slices):
		if i == (num_slices-1)/2:
			slices.append(rows)
		else:
			slices.append(empty_rows)
	active_cubes = []
	inactive_cubes = []
	for slice in range(0,len(slices)):
		for row in range(0,len(slices[slice])):
			for col in range(0, len(slices[slice][row])):
				coordinates = [row, col, slice]
				if slices[slice][row][col] == "#":
					active_cubes.append(coordinates)
				else:
					inactive_cubes.append(coordinates)
	cycle = 1
	possible_changes = list(itertools.product([-1,0,1], repeat = 3))
	possible_changes.remove((0,0,0))
	new_active_cubes = []
	while cycle <= 6:
		temp_inactive_cubes = copy.deepcopy(inactive_cubes)
		# Check active cubes
		for cube in active_cubes:
			# Check neighbors
			active_neighbors = 0
			for change in possible_changes:
				if [cube[0]+change[0],cube[1]+change[1],cube[2]+change[2]] in active_cubes:
					active_neighbors += 1
			if active_neighbors in [2,3]:
				if cube not in new_active_cubes:
					new_active_cubes.append(cube)
			else:
				if cube not in temp_inactive_cubes:
					temp_inactive_cubes.append(cube)
				if cube in new_active_cubes:
					new_active_cubes.remove(cube)
		# Check inactive cubes
		for cube in inactive_cubes:
			# Check neighbors
			active_neighbors = 0
			for change in possible_changes:
				if [cube[0]+change[0],cube[1]+change[1],cube[2]+change[2]] in active_cubes:
					active_neighbors += 1
			if active_neighbors == 3:
				if cube not in new_active_cubes:
					new_active_cubes.append(cube)
				if cube in temp_inactive_cubes:
					temp_inactive_cubes.remove(cube)
		inactive_cubes = temp_inactive_cubes
		active_cubes = copy.deepcopy(new_active_cubes)
		cycle += 1
	print(len(active_cubes))


if __name__ == "__main__":
	print("Part 1:")
	part1()
	#print("\nPart 2:")
	#part2()