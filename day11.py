def part1():
	seats=[]
	with open('inputs/day11.txt') as f:
		for line in f:
			if line != "\n":
				row = list(line.strip("\n"))
				seats.append(row)
	new_seats = []
	for row in range(0,len(seats)):
		new_row = []
		for seat in range(0,len(seats[row])):
			new_row.append(seats[row][seat])
		new_seats.append(new_row)
	reached_last_equal = False
	rounds = 0
	while not reached_last_equal:
		rounds += 1
		for row in range(0, len(seats)):
			for seat in range(0, len(seats[row])):
				if seats[row][seat] == "L":
					all_empty = True
					# to the right
					if seat + 1 < len(seats[row]):
						if seats[row][seat+1] == "#":
							all_empty = False
						# to the bottom right diagonal
						if row + 1 < len(seats):
							if seats[row+1][seat+1] == "#":
								all_empty = False
						# to the top right diagonal
						if row-1 >= 0:
							if seats[row-1][seat+1] == "#":
								all_empty = False
					# to the left
					if seat - 1 >= 0:
						if seats[row][seat-1] == "#":
							all_empty = False
						# to the bottom left diagonal
						if row + 1 < len(seats):
							if seats[row+1][seat-1] == "#":
								all_empty = False
						# to the top right diagonal
						if row-1 >= 0:
							if seats[row-1][seat-1] == "#":
								all_empty = False
					# to the bottom
					if row + 1 < len(seats):
						if seats[row+1][seat] == "#":
							all_empty =False
					# to the top
					if row - 1 >=0:
						if seats[row-1][seat] == "#":
							all_empty = False
					if all_empty:
						new_seats[row][seat] = "#"
				elif seats[row][seat] == "#":
					occupied_seats = 0
					# to the right
					if seat + 1 < len(seats[row]):
						if seats[row][seat+1] == "#":
							occupied_seats += 1
						# to the bottom right diagonal
						if row + 1 < len(seats):
							if seats[row+1][seat+1] == "#":
								occupied_seats += 1
						# to the top right diagonal
						if row-1 >= 0:
							if seats[row-1][seat+1] == "#":
								occupied_seats += 1
					# to the left
					if seat - 1 >= 0:
						if seats[row][seat-1] == "#":
							occupied_seats += 1
						# to the top left diagonal
						if row + 1 < len(seats):
							if seats[row+1][seat-1] == "#":
								occupied_seats += 1
						# to the bottom left diagonal
						if row-1 >= 0:
							if seats[row-1][seat-1] == "#":
								occupied_seats += 1
					# to the bottom
					if row + 1 < len(seats):
						if seats[row+1][seat] == "#":
							occupied_seats += 1
					# to the top
					if row - 1 >= 0:
						if seats[row-1][seat] == "#":
							occupied_seats += 1
					if occupied_seats >= 4:
						new_seats[row][seat] = "L"
		if new_seats == seats:
			reached_last_equal = True
			occupied_seats = 0
			for row in range(0, len(seats)):
				for seat in range(0, len(seats[row])):
					if new_seats[row][seat] == "#":
						occupied_seats += 1
			print(occupied_seats)
		for row in range(0,len(seats)):
			for seat in range(0,len(seats[row])):
				seats[row][seat] = new_seats[row][seat]

def part2():
	seats=[]
	with open('inputs/day11.txt') as f:
		for line in f:
			if line != "\n":
				row = list(line.strip("\n"))
				seats.append(row)
	new_seats = []
	for row in range(0,len(seats)):
		new_row = []
		for seat in range(0,len(seats[row])):
			new_row.append(seats[row][seat])
		new_seats.append(new_row)
	reached_last_equal = False
	rounds = 0
	while not reached_last_equal:
		rounds += 1
		for row in range(0, len(seats)):
			for seat in range(0, len(seats[row])):
				if seats[row][seat] == "L":
					all_empty = True
					# to the right
					right_seat = seat + 1
					while right_seat < len(seats[row]):
						if seats[row][right_seat] != ".":
							if seats[row][right_seat] == "#":
								all_empty = False
								break
							if seats[row][right_seat] == "L":
								break
						right_seat += 1
					# to the left
					left_seat = seat -1
					while left_seat >= 0:
						if seats[row][left_seat] != ".":
							if seats[row][left_seat] == "#":
								all_empty = False
								break
							if seats[row][left_seat] == "L":
								break
						left_seat -= 1
					# to the bottom
					bottom_row = row + 1
					while bottom_row < len(seats):
						if seats[bottom_row][seat] != ".":
							if seats[bottom_row][seat] == "#":
								all_empty = False
								break
							if seats[bottom_row][seat] == "L":
								break
						bottom_row += 1
					# to the top
					top_row = row - 1
					while top_row >= 0:
						if seats[top_row][seat] != ".":
							if seats[top_row][seat] == "#":
								all_empty = False
								break
							if seats[top_row][seat] == "L":
								break
						top_row -= 1
					# diagonally to the top right
					right_seat = seat + 1
					top_row = row - 1
					while right_seat < len(seats[row]) and top_row >=0:
						if seats[top_row][right_seat] != ".":
							if seats[top_row][right_seat] == "#":
								all_empty = False
								break
							if seats[top_row][right_seat] == "L":
								break
						right_seat += 1
						top_row -= 1
					# diagonally to the bottom right
					right_seat = seat + 1
					bottom_row = row + 1
					while right_seat < len(seats[row]) and bottom_row < len(seats):
						if seats[bottom_row][right_seat] != ".":
							if seats[bottom_row][right_seat] == "#":
								all_empty = False
								break
							if seats[bottom_row][right_seat] == "L":
								break
						right_seat += 1
						bottom_row += 1
					# diagonally to the top left
					left_seat = seat - 1
					top_row = row - 1
					while left_seat >=0 and top_row >=0:
						if seats[top_row][left_seat] != ".":
							if seats[top_row][left_seat] == "#":
								all_empty = False
								break
							if seats[top_row][left_seat] == "L":
								break
						left_seat -= 1
						top_row -= 1
					# diagonally to the bottom left
					left_seat = seat - 1
					bottom_row = row + 1
					while left_seat >=0 and bottom_row <len(seats):
						if seats[bottom_row][left_seat] != ".":
							if seats[bottom_row][left_seat] == "#":
								all_empty = False
								break
							if seats[bottom_row][left_seat] == "L":
								break
						left_seat -= 1
						bottom_row += 1
					if all_empty:
						new_seats[row][seat] = "#"
				elif seats[row][seat] == "#":
					occupied_seats = 0
					# to the right
					right_seat = seat + 1
					while right_seat < len(seats[row]):
						if seats[row][right_seat] != ".":
							if seats[row][right_seat] == "#":
								occupied_seats += 1
								break
							if seats[row][right_seat] == "L":
								break
						right_seat += 1
					# to the left
					left_seat = seat -1
					while left_seat >= 0:
						if seats[row][left_seat] != ".":
							if seats[row][left_seat] == "#":
								occupied_seats += 1
								break
							if seats[row][left_seat] == "L":
								break
						left_seat -= 1
					# to the bottom
					bottom_row = row + 1
					while bottom_row < len(seats):
						if seats[bottom_row][seat] != ".":
							if seats[bottom_row][seat] == "#":
								occupied_seats += 1
								break
							if seats[bottom_row][seat] == "L":
								break
						bottom_row += 1
					# to the top
					top_row = row - 1
					while top_row >= 0:
						if seats[top_row][seat] != ".":
							if seats[top_row][seat] == "#":
								occupied_seats += 1
								break
							if seats[top_row][seat] == "L":
								break
						top_row -= 1
					# diagonally to the top right
					right_seat = seat + 1
					top_row = row - 1
					while right_seat < len(seats[row]) and top_row >=0:
						if seats[top_row][right_seat] != ".":
							if seats[top_row][right_seat] == "#":
								occupied_seats += 1
								break
							if seats[top_row][right_seat] == "L":
								break
						right_seat += 1
						top_row -= 1
					# diagonally to the bottom right
					right_seat = seat + 1
					bottom_row = row + 1
					while right_seat < len(seats[row]) and bottom_row < len(seats):
						if seats[bottom_row][right_seat] != ".":
							if seats[bottom_row][right_seat] == "#":
								occupied_seats += 1
								break
							if seats[bottom_row][right_seat] == "L":
								break
						right_seat += 1
						bottom_row += 1
					# diagonally to the top left
					left_seat = seat - 1
					top_row = row - 1
					while left_seat >=0 and top_row >=0:
						if seats[top_row][left_seat] != ".":
							if seats[top_row][left_seat] == "#":
								occupied_seats += 1
								break
							if seats[top_row][left_seat] == "L":
								break
						left_seat -= 1
						top_row -= 1
					# diagonally to the bottom left
					left_seat = seat - 1
					bottom_row = row + 1
					while left_seat >=0 and bottom_row  < len(seats):
						if seats[bottom_row][left_seat] != ".":
							if seats[bottom_row][left_seat] == "#":
								occupied_seats += 1
								break
							if seats[bottom_row][left_seat] == "L":
								break
						left_seat -= 1
						bottom_row += 1
					if occupied_seats >= 5:
						new_seats[row][seat] = "L"
		if new_seats == seats:
			reached_last_equal = True
			occupied_seats = 0
			for row in range(0, len(seats)):
				for seat in range(0, len(seats[row])):
					if new_seats[row][seat] == "#":
						occupied_seats += 1
			print(occupied_seats)
		for row in range(0,len(seats)):
			for seat in range(0,len(seats[row])):
				seats[row][seat] = new_seats[row][seat]

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()