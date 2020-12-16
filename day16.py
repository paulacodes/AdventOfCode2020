import random
def part1():
	rules = []
	rule_index = 0
	with open('inputs/day16.txt') as f:
		for line in f:
			if line != "\n":
				ranges = line.strip("\n").split(": ")[1].split(" or ")
				rules.append([])
				for r in ranges:
					rules[rule_index].append(list(map(int,list(r.split('-')))))
				rule_index += 1
			else:
				break
		nearby_tickets = []
		nearby = False
		for line in f:
			if "nearby tickets:" in line:
				nearby = True
				continue
			if nearby:
				nearby_tickets.append(list(map(int,line.strip("\n").split(","))))
		invalid_value_sum = 0
		invalid_tickets = 0
		for ticket in nearby_tickets:
			for val in range(len(ticket)):
				valid = False
				for rule in range(len(rules)):
					if (ticket[val] >= rules[rule][0][0] \
					and ticket[val] <= rules[rule][0][1]) \
					or (ticket[val] >= rules[rule][1][0] \
					and ticket[val] <= rules[rule][1][1]):
						valid = True
				if not valid:
					invalid_value_sum += ticket[val]
					invalid_tickets += 1
		print(invalid_value_sum)

def part2():
	rules = []
	rule_index = 0
	departure_lines = []
	current_line = 0
	with open('inputs/day16.txt') as f:
		for line in f:
			if line != "\n":
				if "departure" in line:
					departure_lines.append(current_line)
				current_line += 1
				ranges = line.strip("\n").split(": ")[1].split(" or ")
				rules.append([])
				for r in ranges:
					rules[rule_index].append(list(map(int,list(r.split('-')))))
				rule_index += 1
			else:
				break
		nearby_tickets = []
		nearby = False
		your_ticket = []
		yourTicket = False
		for line in f:
			if "your ticket" in line:
				yourTicket = True
				continue
			if "nearby tickets:" in line:
				nearby = True
				continue
			if yourTicket:
				your_ticket = list(map(int,line.strip("\n").split(",")))
				yourTicket = False
			if nearby:
				nearby_tickets.append(list(map(int,line.strip("\n").split(","))))
			current_line += 1
		valid_tickets = []
		for ticket in nearby_tickets:
			invalid_ticket = False
			for val in range(len(ticket)):
				valid = False
				for rule in range(len(rules)):
					if (ticket[val] >= rules[rule][0][0] \
					and ticket[val] <= rules[rule][0][1]) \
					or (ticket[val] >= rules[rule][1][0] \
					and ticket[val] <= rules[rule][1][1]):
						valid = True
				if not valid:
					invalid_ticket = True
					break
			if not invalid_ticket:
				valid_tickets.append(ticket)
		rule_positions = [-1]*len(rules)
		valid_spots = 0
		done = False
		spot_options = {} # used to store the spots that each rule can take up
		for i in range(0,len(rules)):
			spot_options[i] = []
			for j in range(0, len(rules)):
				spot_options[i].append(j)
		# The loop below checks for rules that have only one valid spot. When
		# such a rule is found, its spot is removed from the lists of potential 
		# spots that rules can occupy. The loop ends once each rule has found
		# its unique spot.
		while not done:
			for rule in range(len(rules)):
				valid_spots = 0
				last_seen_spot = 0
				for spot in spot_options[rule]:
					valid = True
					for ticket in valid_tickets:
						if ticket[spot] < rules[rule][0][0] \
						or (ticket[spot] > rules[rule][0][1] \
						and ticket[spot] < rules[rule][1][0]) \
						or ticket[spot] > rules[rule][1][1]:
							valid = False
							break
					if valid:
						last_valid_spot = spot
						valid_spots += 1
				# Upon finding a rule that only has one valid spot, assign 
				# that spot to that rule and remove the spots from the list of 
				# spots that other rules can take
				if valid_spots == 1:
					rule_positions[rule] = last_valid_spot
					for position in spot_options:
						spot_options[position].remove(last_valid_spot)
			if -1 not in rule_positions:
				multiple = 1
				for line in departure_lines:
					multiple = multiple * your_ticket[rule_positions[line]]
				print(multiple)
				done = True

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()