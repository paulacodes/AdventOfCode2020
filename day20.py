import copy

def flip_vertically(tile):
	new_tile = []
	for row in reversed(tile):
		new_tile.append(row)
	return(new_tile)

def flip_horizontally(tile):
	new_tile = []
	tile = copy.deepcopy(list(zip(*reversed(tile))))
	tile = copy.deepcopy(list(zip(*reversed(tile))))
	for row in reversed(tile):
		new_tile.append(row)
	return(new_tile)

def find_matching_right_edges(tile, tiles):
	matching_edges = []
	option = tiles[tile][0]
	for other_tile in tiles:
		if other_tile != tile:
			option_index = 0
			for new_option in tiles[other_tile]:
				option_index += 1
				match = 0
				for i in range(10):
					if option[i][-1] == new_option[i][0]:
						match += 1
				if match == 10:
					matching_edges.append([other_tile,option_index])
	return(matching_edges)

def find_matching_left_edges(tile, tiles):
	matching_edges = []
	option = tiles[tile][0]
	for other_tile in tiles:
		if other_tile != tile:
			option_index = 0
			for new_option in tiles[other_tile]:
				option_index += 1
				match = 0
				for i in range(10):
					if option[i][0] == new_option[i][-1]:
						match += 1
				if match == 10:
					matching_edges.append([other_tile,option_index])
	return(matching_edges)

def find_matching_top_edges(tile, tiles):
	matching_edges = []
	option = tiles[tile][0]
	for other_tile in tiles:
		if other_tile != tile:
			option_index = 0
			for new_option in tiles[other_tile]:
				option_index += 1
				match = 0
				for i in range(10):
					if option[0][i] == new_option[-1][i]:
						match += 1
				if match == 10:
					matching_edges.append([other_tile,option_index])
	return(matching_edges)

def find_matching_bottom_edges(tile, tiles):
	matching_edges = []
	option = tiles[tile][0]
	for other_tile in tiles:
		if other_tile != tile:
			option_index = 0
			for new_option in tiles[other_tile]:
				option_index += 1
				match = 0
				for i in range(10):
					if option[-1][i] == new_option[0][i]:
						match += 1
				if match == 10:
					matching_edges.append([other_tile,option_index])
	return(matching_edges)

def part1():
	tiles = {}
	data = []
	with open('inputs/day20.txt') as f:
		for line in f:
			if "Tile" in line:
				tile = line.split(" ")[1].strip(":\n")
			elif line is not "\n":
				data.append(list(line.strip("\n")))
			else:
				tiles[tile] = data
				data = []
	tiles[tile] = data
	# Generate all possibile orientations of tiles
	new_tiles = copy.deepcopy(tiles)
	for tile in tiles:
		new_tiles[tile] = [new_tiles[tile]]
		new_list = flip_vertically(tiles[tile])
		if new_list not in new_tiles[tile]:
			new_tiles[tile].append(new_list)
		new_list = flip_horizontally(tiles[tile])
		if new_list not in new_tiles[tile]:
			new_tiles[tile].append(new_list)
		rotated_list = copy.deepcopy(tiles[tile])
		for i in range(3):
			rotated_list = copy.deepcopy(list(zip(*reversed(rotated_list))))
			if rotated_list not in new_tiles[tile]:
				new_tiles[tile].append(rotated_list)
			new_list = flip_vertically(rotated_list)
			if new_list not in new_tiles[tile]:
				new_tiles[tile].append(new_list)
			new_list = flip_horizontally(rotated_list)
			if new_list not in new_tiles[tile]:
				new_tiles[tile].append(new_list)
	prod = 1
	# Loop through tiles and multiply tiles with only two sides (corners)
	for tile in new_tiles:
		sides_with_matches = 0
		matches_right = find_matching_right_edges(tile, new_tiles)
		if len(matches_right) > 0:
			sides_with_matches += 1
		matches_left = find_matching_left_edges(tile, new_tiles)
		if len(matches_left) > 0:
			sides_with_matches += 1
		matches_top = find_matching_top_edges(tile, new_tiles)
		if len(matches_top) > 0:
			sides_with_matches += 1
		matches_bottom = find_matching_bottom_edges(tile, new_tiles)
		if len(matches_bottom) > 0:
			sides_with_matches += 1
		if sides_with_matches == 2:
			prod = prod * int(tile)
	print(prod)

if __name__ == "__main__":
	print("Part 1:")
	part1()
	#print("Part 2:")
	#part2()