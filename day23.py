import array

def part1():
	input = "643719258"
	cups = list(map(int, list(input)))
	print(cups)
	current_index = 0
	total_len = len(cups)
	for round in range(100):
		pick_up = []
		current = cups[current_index]
		for i in range(1,4):
			index = (current_index + i)%total_len
			pick_up.append(cups[index])
		for i in pick_up:
			cups.remove(i)
		destination = current - 1
		if destination in cups:
			index = (cups.index(destination)+1)%total_len
			for i in pick_up:
				cups.insert(index,i)
				index = (index+1)%total_len
		else:
			max_cup = max(list(cups))
			min_cup = min(list(cups))
			while destination >= min_cup:
				destination -= 1
				if destination in cups:
					index = (cups.index(destination)+1)%total_len
					for i in pick_up:
						cups.insert(index,i)
						index = (index+1)%total_len
					break
			if destination < min_cup:
				index = (cups.index(max_cup)+1)%total_len
				for i in pick_up:
					cups.insert(index,i)
					index  = (index+1)%total_len
		current_index = (cups.index(current) + 1)%total_len
	print(''.join(list(map(str,cups))).split("1")[1]+''.join(list(map(str,cups))).split("1")[0])
	 
def part2():
	input = "643719258"
	total_len = 1000000
	rounds = 10000000
	next = array.array("i", range(1, total_len + 2))
	cups = array.array("i", map(int, input))

	next[0] = next[-1] = cups[0]
	for i in range(len(cups) - 1):
		next[cups[i]] = cups[i + 1]
	if total_len == len(cups):
		next[cups[len(cups) - 1]] = cups[0]  
	else:
		next[cups[len(cups) - 1]] = max(cups) + 1

	current = 0
	for round in range(rounds):
		current = next[current]
		if current != 1:
			destination = current - 1 
		else:
			destination = total_len
		cup1 = next[current]
		cup2 = next[cup1]
		cup3 = next[cup2]
		while destination == cup1 or destination == cup2 or destination == cup3:
			destination -= 1
		if destination < 1:
			destination += total_len
		next[cup3], next[destination], next[current] = next[destination], next[current], next[cup3]

	if total_len < 10:
		i = next[1]
		while i != 1:
			print(i, end='')
			i = next[i]
		print()
	else:
		print(next[1] * next[next[1]])

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("Part 2:")
	part2()