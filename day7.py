def path_exists(bags, start_bag, path=[]):
	'''
	path_exists takes a dict of bags and a bag, and determines, through
	backtracking, if there are any paths between that bag and a shiny gold
	bag, returing True if there is and False otherwise
	:param bags: dict of bags where each bag contains a list of strings which
	represent bags
	:param start_bag: the bag that we start looking for a path from
	:param path: path passed throughout subsequent calls of the function
	'''
	path = path + [start_bag]
	if start_bag == "shiny gold":
		return [start_bag]
	if start_bag not in bags:
		return []
	paths = []
	for child in bags[start_bag]:
		if child not in path:
			newpath = path_exists(bags, child, path)
			if newpath:
				return True
	return False

def dfs_bag_count(bags, current_bag):
	'''
	dfs_bag_count takes a dict of bags and a bag, and determines, using 
	depth-first search, how many bags that bag contains, and returns that value.
	:param bags: dict of bags where each bag contains a list of dicts which
	represent bags, with the key being the name of the bag and the value the
	amount of bags
	:param current_bag: bag we are currently counting 
	'''
	bag = bags[current_bag]
	child_bag_count = []
	for child in bag:
		child_bag_count.append(bag[child])
		child_bag_count.append(dfs_bag_count(bags, child) * bag[child])
	return sum(child_bag_count)

def part1():
	bags = {}
	with open('inputs/day7.txt') as f:
		for line in f:
			if line != "\n":
				outer_bag = line.split(" bags contain")[0]
				inner_bags = line.split(" bags contain ")[1].replace(".","")
				bag_array = inner_bags.split(", ")
				bag_list = []
				if "no other bags" in inner_bags:
					bags[outer_bag] = []
				else:
					for bag in bag_array:
						individual_bag_array = bag.split(" ")
						color = individual_bag_array[1] + " " + \
						individual_bag_array[2]
						bag_list.append(color)
					bags[outer_bag] = bag_list					
	shiny_gold_count = 0
	valid_bags = []
	for bag in bags:
		can_contain_bag = False
		for child in bags[bag]:
			if path_exists(bags, child):
				can_contain_bag = True
		if can_contain_bag:
			shiny_gold_count += 1
	print(shiny_gold_count)

def part2():
	bags = {}
	with open('inputs/day7.txt') as f:
		for line in f:
			if line != "\n":
				outer_bag = line.split(" bags contain")[0]
				inner_bags = line.split(" bags contain ")[1].replace(".","")
				bag_array = inner_bags.split(", ")
				bag_dict = {}
				if "no other bags" in inner_bags:
					bags[outer_bag] = {}
				else:
					for bag in bag_array:
						individual_bag_array = bag.split(" ")
						number_of_bags = int(individual_bag_array[0])
						color = individual_bag_array[1] + " " + individual_bag_array[2]
						bag_dict[color] = number_of_bags
					bags[outer_bag] = bag_dict					
		shiny_gold_count = dfs_bag_count(bags, 'shiny gold')
		print(shiny_gold_count)

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()