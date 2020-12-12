def part1():
	directions = []
	horizontal = 0
	vertical = 0
	horizontal_direction = -1
	vertical_direction = 1
	degrees = 0
	degree_mapping = {
		0: "E",
		90: "S",
		180: "W",
		270: "N"
	}
	direction_mapping = {
		"E": -1,
		"S": -1 ,
		"W": 1,
		"N": 1
	}
	with open('inputs/day12.txt') as f:
		for line in f:
			if line != "\n":
				direction = str(line.strip("\n"))
				directions.append([direction[0], int(direction[1:len(direction)])])
	for direction in directions:
		if direction[0] == "N":
			vertical += direction[1]
		elif direction[0] == "S":
			vertical -= direction[1]
		elif direction[0] == "E":
			horizontal -= direction[1]
		elif direction[0] == "W":
			horizontal += direction[1]
		elif direction[0] == "F":
			if degree_mapping[degrees] in ["E", "W"]:
				horizontal += horizontal_direction * direction[1]
			else:
				vertical += vertical_direction * direction[1]
		elif direction[0] == "L":
			degrees = (degrees - direction[1])%360
			if degree_mapping[degrees] in ["E", "W"]:
				horizontal_direction = direction_mapping[degree_mapping[degrees]]
			else:
				vertical_direction = direction_mapping[degree_mapping[degrees]]
		elif direction[0] == "R":
			degrees =(degrees + direction[1])%360
			if degree_mapping[degrees] in ["E", "W"]:
				horizontal_direction = direction_mapping[degree_mapping[degrees]]
			else:
				vertical_direction = direction_mapping[degree_mapping[degrees]]
	print(abs(horizontal) + abs(vertical))

def part2():
	directions = []
	horizontal = 0
	vertical = 0
	waypoint_horizontal = -10
	waypoint_vertical = 1
	waypoint_degrees = 0
	with open('inputs/day12.txt') as f:
		for line in f:
			if line != "\n":
				direction = str(line.strip("\n"))
				directions.append([direction[0], int(direction[1:len(direction)])])
	for direction in directions:
		if direction[0] == "N":
			waypoint_vertical += direction[1]
		elif direction[0] == "S":
			waypoint_vertical -= direction[1]
		elif direction[0] == "E":
			waypoint_horizontal -= direction[1]
		elif direction[0] == "W":
			waypoint_horizontal += direction[1]
		elif direction[0] == "F":
			horizontal += waypoint_horizontal * direction[1]
			vertical += waypoint_vertical * direction[1]
		elif direction[0] == "L":
			waypoint_degrees = (waypoint_degrees - direction[1])%360
			if direction[1] == 90:
				temp = waypoint_horizontal
				waypoint_horizontal = waypoint_vertical
				waypoint_vertical = (-1) * temp
			if direction[1] == 180:
				waypoint_horizontal = (-1) * waypoint_horizontal
				waypoint_vertical = (-1) * waypoint_vertical
			if direction[1] == 270:
				temp = waypoint_horizontal
				waypoint_horizontal = (-1) * waypoint_vertical
				waypoint_vertical = temp
		elif direction[0] == "R":
			waypoint_degrees = (waypoint_degrees + direction[1])%360
			if direction[1] == 90:
				temp = waypoint_horizontal
				waypoint_horizontal = (-1) * waypoint_vertical
				waypoint_vertical = temp
			if direction[1] == 180:
				waypoint_horizontal = (-1) * waypoint_horizontal
				waypoint_vertical = (-1) * waypoint_vertical
			if direction[1] == 270:
				temp = waypoint_horizontal
				waypoint_horizontal = waypoint_vertical
				waypoint_vertical = (-1) * temp
	print(abs(horizontal) + abs(vertical))


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()