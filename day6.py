def check_yes_count(group_answer):
	"""
	check_yes_count takes the answers belonging to a group of passengers and 
	returns the number of unique questions answered with a yes
	:param group_answer: all the group answers as a string
	"""
	answers = {}
	for char in group_answer:
		answers[char] = True
	return(len(answers))

def check_yes_from_everyone_count(group_answer, people_in_group):
	"""
	check_yes__from_everyone_count takes the answers belonging to a group of 
	passengers and returns the number of unique questions that everyone in the 
	roup answered with a yes
	:param group_answer: all the group answers as a string
	:param people_in_group: number of people in the group
	"""
	answers = {}
	yes_answers = 0
	for answer in group_answer:
		answer_list = list(answer)
		answers_no_dups = set(answer_list)
		for char in answers_no_dups:
			if char in answers:
				answers[char] += 1
				if answers[char] == people_in_group:
					yes_answers += 1
			else:
				answers[char] = 1
	return(yes_answers)


def part1():
	sum_counts = 0
	with open('inputs/day6.txt') as f:
		group_answer = ""
		for line in f:
			if line != "\n":
				group_answer += line.strip("\n")
			else:
				sum_counts += check_yes_count(group_answer)
				group_answer = ""
		sum_counts += check_yes_count(group_answer)
	print(sum_counts)


def part2():
	sum_counts = 0
	with open('inputs/day6.txt') as f:
		group_answer = []
		people_in_group = 0
		for line in f:
			if line != "\n":
				group_answer.append(line.strip("\n"))
				people_in_group += 1
			else:
				sum_counts += check_yes_from_everyone_count(group_answer, 
					people_in_group)
				group_answer = []
				people_in_group = 0
		sum_counts += check_yes_from_everyone_count(group_answer, 
			people_in_group)
	print(sum_counts)


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()