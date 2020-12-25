from copy import deepcopy

move_mapping = {
	'e' : ( 4,  0),
	'w' : (-4,  0),
	'nw': (-2, -3),
	'ne': ( 2, -3),
	'sw': (-2,  3),
	'se': ( 2,  3),
}

def find_neighbors(tile):
	neighbors = []
	for move in move_mapping:
		neighbors.append((tile[0] + move_mapping[move][0], tile[1] + move_mapping[move][1]))
	return(neighbors)

def part1():
	instructions = []
	with open('inputs/day24.txt') as f:
		for line in f:
			instruction = line.strip("\n")
			directions = []
			index = 0
			while index < len(instruction):
				if instruction[index] == "e":
					directions.append("e")
				elif instruction[index] == "s":
					index += 1
					if instruction[index] == "e":
						directions.append("se")
					else:
						directions.append("sw")
				elif instruction[index] == "w":
					directions.append("w")
				elif instruction[index] == "n":
					index += 1
					if instruction[index] == "e":
						directions.append("ne")
					else:
						directions.append("nw")
				index += 1
			instructions.append(directions)
	white_tiles = set()
	black_tiles = set()
	white_tiles.add((0,0))
	for instruction in instructions:
		horizontal = 0
		vertical = 0
		for move in instruction:
			horizontal += move_mapping[move][0]
			vertical += move_mapping[move][1]
		position = (horizontal, vertical)
		if position in white_tiles:
			black_tiles.add(position)
			white_tiles.remove(position)
		elif position in black_tiles:
			white_tiles.add(position)
			black_tiles.remove(position)
		else:
			black_tiles.add(position)
	print(len(black_tiles))

def part2():
	instructions = []
	with open('inputs/day24.txt') as f:
		for line in f:
			instruction = line.strip("\n")
			directions = []
			index = 0
			while index < len(instruction):
				if instruction[index] == "e":
					directions.append("e")
				elif instruction[index] == "s":
					index += 1
					if instruction[index] == "e":
						directions.append("se")
					else:
						directions.append("sw")
				elif instruction[index] == "w":
					directions.append("w")
				elif instruction[index] == "n":
					index += 1
					if instruction[index] == "e":
						directions.append("ne")
					else:
						directions.append("nw")
				index += 1
			instructions.append(directions)
	white_tiles = set()
	black_tiles = set()
	white_tiles.add((0,0))
	for instruction in instructions:
		horizontal = 0
		vertical = 0
		for move in instruction:
			horizontal += move_mapping[move][0]
			vertical += move_mapping[move][1]
		position = (horizontal, vertical)
		if position in white_tiles:
			black_tiles.add(position)
			white_tiles.remove(position)
		elif position in black_tiles:
			white_tiles.add(position)
			black_tiles.remove(position)
		else:
			black_tiles.add(position)
	for day in range(100):
		new_black_tiles = set()
		new_white_tiles = set()
		for tile in black_tiles:
			black = 0
			for neighbor in find_neighbors(tile):
				if neighbor in black_tiles:
					black += 1
				white_tiles.add(neighbor)
			if black == 0 or black > 2:
				new_white_tiles.add(tile)
			else:
				new_black_tiles.add(tile)
		for tile in white_tiles:
			black = 0
			for neighbor in find_neighbors(tile):
				if neighbor in black_tiles:
					black += 1
			if black == 2:
				new_black_tiles.add(tile)
			else:
				new_white_tiles.add(tile)
		black_tiles = deepcopy(new_black_tiles)
		white_tiles = deepcopy(new_white_tiles)
	print(len(black_tiles))

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("Part 2:")
	part2()