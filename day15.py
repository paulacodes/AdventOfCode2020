def play_game(turns):
	input = "0,13,1,16,6,17"
	numbers = list(map(int, input.split(",")))
	turn = 1
	numbers_and_turns = {}
	numbers_and_turns2 = {}
	last_num = 0
	for num in numbers:
		numbers_and_turns[num] = turn
		last_num = num
		turn += 1
	skipCheck = False
	while turn <= turns:
		if last_num not in numbers_and_turns2:
			if skipCheck:
				numbers_and_turns[0] = numbers_and_turns2[0]
			elif 0 in numbers_and_turns2:
				numbers_and_turns[0] = numbers_and_turns2[0]
				skipCheck = True
			numbers_and_turns2[0] = turn
			last_num = 0
		else:
			difference = numbers_and_turns2[last_num] - numbers_and_turns[last_num]
			if difference in numbers_and_turns:
				if difference in numbers_and_turns2:
					numbers_and_turns[difference] = numbers_and_turns2[difference]
				numbers_and_turns2[difference] = turn
			else:
				numbers_and_turns[difference] = turn
			last_num = difference
		turn += 1
	return(last_num)

def part1():
	print(play_game(2020))

def part2():
	print(play_game(30000000))

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()