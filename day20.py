import copy
from heapq import nsmallest

def flipped(listtree):
    return [(flipped(x) if isinstance(x, list) else x)
                             for x in reversed(listtree)]
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
	for option in tiles[tile]:
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
	for option in tiles[tile]:
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
	for option in tiles[tile]:
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
	for option in tiles[tile]:
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

	value_matches_dict = {}
	matches_dict = {}
	for tile in new_tiles:
		matches = find_matching_right_edges(tile, new_tiles)
		matches = find_matching_left_edges(tile, new_tiles)
		matches = find_matching_top_edges(tile, new_tiles)
		matches = find_matching_bottom_edges(tile, new_tiles)
		value_matches_dict[tile] = len(matches)
		matches_dict[tile] = matches

	corners = nsmallest(4, value_matches_dict, key = value_matches_dict.get)
	prod = 1
	for corner in corners:
		prod *= int(corner)
	print(prod)


		


if __name__ == "__main__":
	print("Part 1:")
	part1()
	#print("Part 2:")
	#part2()