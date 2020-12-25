def get_loops(key):
	result = 1
	loops = 0
	while result != key:
		result *= 7
		result = result%20201227
		loops += 1
	return loops

with open('inputs/day25.txt') as f:
	for line1, line2 in zip(f, f):
		card_key = int(line1)
		door_key = int(line2)

card_loops = get_loops(card_key)

door_loops = get_loops(door_key)

door_result = 1

for _ in range(card_loops):
	door_result *= door_key
	door_result = door_result%20201227

print(door_result)
