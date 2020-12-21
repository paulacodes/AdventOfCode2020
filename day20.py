import copy
from math import sqrt
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

def find_matching_right_edges(tile, tiles, position = 0, used_tiles = []):
	matching_edges = []
	option = tiles[tile][position]
	for other_tile in tiles:
		if other_tile != tile and other_tile not in used_tiles:
			option_index = 0
			for new_option in tiles[other_tile]:
				match = 0
				for i in range(10):
					if option[i][-1] == new_option[i][0]:
						match += 1
				if match == 10:
					matching_edges.append([other_tile,option_index])
				option_index += 1
	return(matching_edges)

def find_matching_left_edges(tile, tiles, position = 0, used_tiles = []):
	matching_edges = []
	option = tiles[tile][position]
	for other_tile in tiles:
		if other_tile != tile and other_tile not in used_tiles:
			option_index = 0
			for new_option in tiles[other_tile]:
				match = 0
				for i in range(10):
					if option[i][0] == new_option[i][-1]:
						match += 1
				if match == 10:
					matching_edges.append([other_tile,option_index])
				option_index += 1
	return(matching_edges)

def find_matching_top_edges(tile, tiles, position = 0, used_tiles = []):
	matching_edges = []
	option = tiles[tile][position]
	for other_tile in tiles:
		if other_tile != tile and other_tile not in used_tiles:
			option_index = 0
			for new_option in tiles[other_tile]:
				match = 0
				for i in range(10):
					if option[0][i] == new_option[-1][i]:
						match += 1
				if match == 10:
					matching_edges.append([other_tile,option_index])
				option_index += 1
	return(matching_edges)

def find_matching_bottom_edges(tile, tiles, position = 0, used_tiles = []):
	matching_edges = []
	option = tiles[tile][position]
	for other_tile in tiles:
		if other_tile != tile and other_tile not in used_tiles:
			option_index = 0
			for new_option in tiles[other_tile]:
				match = 0
				for i in range(10):
					if option[-1][i] == new_option[0][i]:
						match += 1
				if match == 10:
					matching_edges.append([other_tile,option_index])
				option_index += 1
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
	total_number_of_rows = int(sqrt(len(tiles)))
	print(total_number_of_rows)
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

def part2():
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
	total_number_of_rows = int(sqrt(len(tiles)))
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
	# Loop through tiles and get first tile with only two sides (a corner)
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
			corner_slide = tile
			break
	position = 0
	used_tiles = []
	used_tiles.append(tile)
	first_row = [[] for _ in range(total_number_of_rows)]
	full_image = [[[] for _ in range(total_number_of_rows)] for _ in range(total_number_of_rows)]
	full_image_names_and_positions = [[[] for _ in range(total_number_of_rows)] for _ in range(total_number_of_rows)]

	first_row[total_number_of_rows-1] = new_tiles[tile]
	first_row_tile_names_and_positions = [[] for _ in range(total_number_of_rows)]
	first_row_tile_names_and_positions[total_number_of_rows-1] = [tile, position]

	for i in range(total_number_of_rows-1):
		matching_edges = find_matching_left_edges(tile, new_tiles, position, used_tiles)
		if len(matching_edges) > 0:
			tile = matching_edges[0][0]
			position = matching_edges[0][1]
			used_tiles.append(tile)
			index = total_number_of_rows - 1 - i
			first_row[index-1] = new_tiles[tile]
			#print(new_tiles[tile])
			first_row_tile_names_and_positions[index-1] = [tile,position]
		else:
			break

	#full_image[0] = first_row
	#full_image_names_and_positions[0] = first_row_tile_names_and_positions
	for spot in range(len(first_row)):
		tile = first_row_tile_names_and_positions[spot][0]
		full_image[0][spot] = tiles[tile]
		position = first_row_tile_names_and_positions[spot][1]
		for i in range(1,total_number_of_rows):
			matching_edges = find_matching_bottom_edges(tile, new_tiles, position, used_tiles)
			if len(matching_edges) > 0:
				tile = matching_edges[0][0]
				position = matching_edges[0][1]
				used_tiles.append(tile)
				full_image[i][spot] = tiles[tile]
			else:
				print("NO MATCH")
				break
	final_rows = []
	for row_of_tiles in full_image:
		rows = [[] for _ in range(10)]
		for tile in row_of_tiles:
			for row in range(len(tile)):
				if row != 0 and row != 9:
					for char in range(len(tile[row])):
						if char != 0 and char != 9:
							rows[row].append(tile[row][char])
		for i in rows:
			if len(i) > 0:
				final_rows.append(i)
	print(len(final_rows))
	print(len(final_rows[0]))
	final_row_variations = []
	final_row_variations.append(final_rows)
	final_row_variations.append(flip_vertically(final_rows))
	final_row_variations.append(flip_horizontally(final_rows))
	rotated_list = copy.deepcopy(final_rows)
	for i in range(3):
		rotated_list = copy.deepcopy(list(zip(*reversed(rotated_list))))
		if rotated_list not in final_row_variations:
			final_row_variations.append(rotated_list)
		new_list = flip_vertically(rotated_list)
		if new_list not in final_row_variations:
			final_row_variations.append(new_list)
		new_list = flip_horizontally(rotated_list)
		if new_list not in final_row_variations:
			final_row_variations.append(new_list)
	for variation in final_row_variations:
		for row in range(1,len(variation)-1):
			for col in range(0, len(variation[row])-19):
				if variation[row][col] == "#" and variation[row][col+5] == "#" and variation[row][col+6] == "#" \
				and variation[row][col + 11] == "#" and variation[row][col + 12] == "#" and variation[row][col+17] == "#" \
				and variation[row][col+18] == "#" and variation[row][col+19]=="#" and variation[row-1][col+18] == "#" \
				and variation[row+1][col+1] == "#" and variation[row+1][col+4]=="#" and variation[row+1][col+7] == "#" \
				and variation[row+1][col+10] == "#" and variation[row+1][col+13]=="#" and variation[row+1][col+16] == "#":
					print("MONSTER FOUND")

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("Part 2:")
	part2()