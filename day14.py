from numpy import binary_repr
from itertools import product

def part1():
	mem = {}
	with open('inputs/day14.txt') as f:
		for line in f:
			if "mask" in line:
				mask = line.split(" = ")[1].strip("\n")
			else:
				index = int(line.split(" = ")[0].split("[")[1].strip("] "))
				value = str(binary_repr(int(line.split(" = ")[1].strip("\n")), width = 36))
				mem[index] = [value, mask]
	sum = 0
	for index in mem:
		value = mem[index][0]
		mask = mem[index][1]
		new_value = ""
		for bit in range(0,len(mask)):
			if mask[bit] in ["0", "1"]:
				new_value += mask[bit]
			else:
				new_value += value[bit]
		sum += int(new_value,2)
	print(sum)

def part2():
	mem = []
	with open('inputs/day14.txt') as f:
		for line in f:
			if "mask" in line:
				mask = line.split(" = ")[1].strip("\n")
			else:
				index = int(line.split(" = ")[0].split("[")[1].strip("] "))
				value = str(binary_repr(int(line.split(" = ")[1].strip("\n")), width = 36))
				mem.append([index, value, mask])
	new_mem = {}
	for triplet in mem:
		address = str(binary_repr(triplet[0], width = 36))
		value = triplet[1]
		mask = triplet[2]
		new_index = ""
		floating_bits = []
		for bit in range(0,len(mask)):
			if mask[bit] == "1":
				new_index += "1"
			elif mask[bit] == "0":
				new_index += address[bit]
			else:
				new_index += "{}"
				floating_bits.append(bit)
		options = list(product(["0","1"], repeat = len(floating_bits)))
		for option in options:
			updated_index = new_index.format(*"".join(option))
			updated_index = int(updated_index,2)
			new_mem[updated_index] = [value,mask]
	sum = 0
	for index in new_mem:
		sum += int(new_mem[index][0],2)
	print(sum)

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()