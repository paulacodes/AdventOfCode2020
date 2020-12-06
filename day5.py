import math

def find_row(seat):
	"""
	find_row returns the row of a seat based off of a 10-characer seat representation
	:param seat: the string representation of a seat
	"""
	lowest_row = 0
	highest_row = 127
	for char in seat[0:7]:
		if highest_row - lowest_row == 1:
			if char == "F":
				return(lowest_row)
			else:
				return(highest_row)
		else:
			updated_row = highest_row - (highest_row-lowest_row)/2
			if char == "F":
				highest_row = math.floor(updated_row)
			elif char == "B":
				lowest_row = math.ceil(updated_row)
	return 0
		
def find_column(seat):
	"""
	find_column returns the column of a seat based off of a 10-characer seat 
	representation
	:param seat: the string representation of a seat
	"""
	lowest_col = 0
	highest_col = 7
	for char in seat[7:10]:
		if highest_col- lowest_col == 1:
			if char == "L":
				return(lowest_col)
			else:
				return(highest_col)
		else:
			updated_col = highest_col - (highest_col - lowest_col)/2
			if char == "L":
				highest_col = math.floor(updated_col)
			elif char == "R":
				lowest_col = math.ceil(updated_col)

def part1():
	with open('inputs/day5.txt') as f:
		highest_seat_id = 0
		for line in f:
			seat = line.strip("\n")
			final_row = find_row(seat)
			final_col = find_column(seat)
			unique_seat_id = final_row * 8 + final_col
			if unique_seat_id > highest_seat_id:
				highest_seat_id = unique_seat_id
	f.close()
	print("Highest seat id:", str(highest_seat_id))

def part2():
	unique_ids = []
	with open('inputs/day5.txt') as f:
		for line in f:
			seat = line.strip("\n")
			final_row = find_row(seat)
			final_col = find_column(seat)
			unique_seat_id = final_row * 8 + final_col
			unique_ids.append(unique_seat_id)
		unique_ids.sort()
	f.close()
	for unique_id in range(1,len(unique_ids)-1):
		if unique_ids[unique_id] + 1 not in unique_ids:
			print("Your seat is:", str(unique_ids[unique_id]+1))

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()




