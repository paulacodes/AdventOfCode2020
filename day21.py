def part1():
	allergens = {}
	with open('inputs/day21.txt') as f:
		allergens = {}
		all_ingredients = []
		for line in f:
			ingredients = line.split(" (")[0].split(" ")
			all_ingredients.extend(ingredients)
			allergen_list = line.split("contains ")[1].strip(")\n").split(", ")
		# Get possible ingredients for each allergen by intersecting the 
		# sets of ingredients associated with it. 
		for allergen in allergen_list:
			if allergen not in allergens:
				allergens[allergen] = set()
				for ingredient in ingredients:
					allergens[allergen].add(ingredient)
			else:
				allergens[allergen] = allergens[allergen].intersection(ingredients)
		no_allergen_ingredients = 0
		# Get ingredients not associated with any allergens
		for ingredient in all_ingredients:
			found = False
			for allergen in allergens:
				if ingredient in allergens[allergen]:
					found = True
					break
			if not found:
				no_allergen_ingredients += 1
		print(no_allergen_ingredients)

def part2():
	allergens = {}
	with open('inputs/day21.txt') as f:
		allergens = {}
		all_ingredients = []
		for line in f:
			ingredients = line.split(" (")[0].split(" ")
			all_ingredients.extend(ingredients)
			allergen_list = line.split("contains ")[1].strip(")\n").split(", ")
			for allergen in allergen_list:
				if allergen not in allergens:
					allergens[allergen] = set()
					for ingredient in ingredients:
						allergens[allergen].add(ingredient)
				else:
					allergens[allergen] = allergens[allergen].intersection(ingredients)
	ingredient_map = {}
	# Get possible allergens for each ingredient
	for allergen in allergens:
		for ingredient in allergens[allergen]:
			if ingredient not in ingredient_map:
				ingredient_map[ingredient] = [allergen]
			else:
				ingredient_map[ingredient].append(allergen)
	allergen_ingredient_pairs = []
	taken_allergens = []
	all_matches_found = False
	while not all_matches_found:
		for ingredient in ingredient_map:
			# Find ingredients with only one possible allergen and add allergen
			# to list of taken allergens
			if len(ingredient_map[ingredient]) == 1:
				allergen_ingredient_pairs.append([ingredient_map[ingredient][0], ingredient])
				taken_allergens.append(ingredient_map[ingredient][0])
				ingredient_map[ingredient].remove(ingredient_map[ingredient][0])
			else:
				# Remove taken allergens from other allergens
				for allergen in taken_allergens:
					if allergen in ingredient_map[ingredient]:
						ingredient_map[ingredient].remove(allergen)
		if len(allergen_ingredient_pairs) == len(ingredient_map):
			all_matches_found = True
	allergen_ingredient_pairs.sort()
	dangerous_ingredients = []
	for pair in allergen_ingredient_pairs:
		dangerous_ingredients.append(pair[1])
	print(','.join(map(str,dangerous_ingredients)))

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("Part 2:")
	part2()