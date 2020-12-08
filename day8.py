def find_end_game(instructions, numbers, part):
	'''
	Finds the "end game" based on an array of instructions and an array of 
	numbers. For part 1, end game comes when we reach an instruction again,
	in which case the current accumulator value is returned. For part 2, end
	game comes when we find an end game that goes till the end of the file,
	in which case we return the accumulator value, otherwise returning -1.
	:param instructions: array of instructions
	:param numbers: array of integers associated with the instructions
	:param part: the part that the function is being used for
	'''
	keep_going = True
	seen_steps = []
	acc = 0
	current_step = 0
	max_number = 0
	while(keep_going):
		seen_steps.append(current_step)
		instruction = instructions[current_step]
		number = numbers[current_step]
		if instruction == "acc":
			acc += number
			current_step += 1
		elif instruction == "jmp":
			current_step += number
		elif instruction == "nop":
			current_step += 1
		if current_step in seen_steps:
			keep_going = False
			if part == 1:
				return acc
		if current_step == len(instructions):
			if part == 2:
				return acc
	return -1 

def part1():
	instructions = []
	numbers = []
	with open('inputs/day8.txt') as f:
		for line in f:
			if line != "\n":
				step = line.strip("\n")
				instructions.append(step.split(" ")[0])
				numbers.append(int(step.split(" ")[1]))
	print(find_end_game(instructions, numbers, 1))

def part2():
	instructions = []
	numbers = []
	nop_positions = []
	jmp_positions = []
	with open('inputs/day8.txt') as f:
		line_number = 0
		for line in f:
			if line != "\n":
				step = line.strip("\n")
				instructions.append(step.split(" ")[0])
				numbers.append(int(step.split(" ")[1]))
				if instructions[line_number] == "nop":
					nop_positions.append(line_number)
				if instructions[line_number] == "jmp":
					jmp_positions.append(line_number)
				line_number += 1
	for position in nop_positions:
		instructions[position] = "jmp"
		result = find_end_game(instructions, numbers, 2)
		if result > -1:
			print(result)
		instructions[position] = "nop"

	for position in jmp_positions:
		instructions[position] = "nop"
		result = find_end_game(instructions, numbers, 2)
		if result > -1:
			print(result)
		instructions[position] = "jmp"


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()