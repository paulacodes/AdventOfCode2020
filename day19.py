import itertools

def get_all_possibilities_for_rule(rule, rules):
	'''
	get_all_possibilities_for_rule generates all the possible values
	that follow a specific rule
	:param rule: the int value of the rule we're checking
	: param rules: the total rules given as input
	'''
	possibilities = {}

	if rule in ('"a"', '"b"'):
		return set(rule[1])

	if ' ' not in rule:
		return get_all_possibilities_for_rule(rules[int(rule)], rules)

	if rule in possibilities:
		return possibilities[rule]

	if '|' not in rule:
		tokens = rule.split(' ')
		possible = get_all_possibilities_for_rule(rules[int(tokens[0])], rules)
		for r in tokens[1:]:
			additional = get_all_possibilities_for_rule(rules[int(r)], rules)
			possible = set(a + b for a, b in itertools.product(possible, additional))
		possibilities[rule] = possible
		return possible

	else:
		i = rule.find('|')
		lhs = get_all_possibilities_for_rule(rule[:i-1], rules)
		rhs = get_all_possibilities_for_rule(rule[i+2:], rules)
		possible = lhs.union(rhs)
		possibilities[rule] = possible
		return possible

def get_values_ending_in_message(message, values):
	'''
	get_messages_ending_in_value returns the number of values that end
	with a specific message
	:param message: the message that we're checking against
	"param values: list of values
	'''
	matches = 0
	while True:
		match = False
		for value in values:
			if message.endswith(value):
				match = True
				break
		if not match:
			return matches
		else:
			matches += 1
			message = message[:-8]

def part1():
	rules = {}
	messages = []
	with open('inputs/day19.txt') as f:
		for line in f:
			if ":" in line:
				rules[int(line.split(": ")[0])] = line.split(": ")[1].strip("\n")
			elif line is not "\n":
				messages.append(line.strip("\n"))
	possibilities = get_all_possibilities_for_rule(rules[0], rules)
	matches = 0
	for message in messages:
		if message in possibilities:
			matches += 1
	print(matches)

def part2():
	rules = {}
	messages = []
	with open('inputs/day19.txt') as f:
		for line in f:
			if ":" in line:
				rules[int(line.split(": ")[0])] = line.split(": ")[1].strip("\n")
			elif line is not "\n":
				messages.append(line.strip("\n"))
	possibilities = get_all_possibilities_for_rule(rules[0], rules)
	matches = 0
	values_42 = get_all_possibilities_for_rule("42", rules)
	values_31 = get_all_possibilities_for_rule("31", rules)
	for message in messages:
		ending_31 = get_values_ending_in_message(message, values_31)
		message = message[:-8 * ending_31]
		ending_42 = get_values_ending_in_message(message, values_42)
		if ending_42 * 8 == len(message) and ending_42 > ending_31:
			matches += 1
	print(matches)


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("Part 2:")
	part2()
