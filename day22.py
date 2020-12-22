from collections import deque
from itertools import islice

def recursive_combat(player1deque, player2deque):
	player1used = set()
	player2used = set()

	while len(player1deque)>0 and len(player2deque)>0:

		if tuple(player1deque) in player1used:
			return (player1deque, 1)
		else:
			player1used.add(tuple(player1deque))
			player2used.add(tuple(player2deque))

		player1 = player1deque.popleft()
		player2 = player2deque.popleft()

		recursive_score = None

		if player1 <= len(player1deque) and player2 <= len(player2deque):
			player1deque_rec = deque(islice(player1deque, 0, player1))
			player2deque_rec = deque(islice(player2deque, 0, player2))
			recursive_score = recursive_combat(player1deque_rec, player2deque_rec)[1]

		if recursive_score == 1:
			player1deque.extend((player1, player2))
		elif recursive_score == 2:
			player2deque.extend((player2, player1))
		elif player1 > player2:
			player1deque.extend((player1, player2))
		elif player2 > player1:
			player2deque.extend((player2, player1))

	if len(player1deque) > 0:
		return(player1deque, 1)
	else:
		return(player2deque, 2)

def part1():
	player1 = False
	player1cards = []
	player2 = False
	player2cards = []
	with open('inputs/day22.txt') as f:
		for line in f:
			if "Player 1" in line:
				player1 = True
			elif "Player 2" in line:
				player1 = False
				player2 = True
			elif player1 and line!= "\n":
				player1cards.append(int(line.strip("\n")))
			elif player2 and line!= "\n":
				player2cards.append(int(line.strip("\n")))
	player1deque = deque(player1cards)
	player2deque = deque(player2cards)

	while len(player1deque) > 0 and len(player2deque) > 0:
		if player1deque[0]>player2deque[0]:
			player1deque.append(player1deque.popleft())
			player1deque.append(player2deque.popleft())
		else:
			player2deque.append(player2deque.popleft())
			player2deque.append(player1deque.popleft())

	score = 0
	multiple = 1
	while len(player1deque)>0:
		score += player1deque[-1]*multiple
		multiple += 1
		player1deque.pop()
	print(score)

def part2():
	player1 = False
	player1cards = []
	player2 = False
	player2cards = []
	with open('inputs/day22.txt') as f:
		for line in f:
			if "Player 1" in line:
				player1 = True
			elif "Player 2" in line:
				player1 = False
				player2 = True
			elif player1 and line!= "\n":
				player1cards.append(int(line.strip("\n")))
			elif player2 and line!= "\n":
				player2cards.append(int(line.strip("\n")))
	player1deque = deque(player1cards)
	player2deque = deque(player2cards)
	deck = recursive_combat(player1deque, player2deque)[0]
	score = 0
	multiple = 1
	while len(deck)>0:
		score += deck[-1]*multiple
		multiple += 1
		deck.pop()
	print(score)

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("Part 2:")
	part2()