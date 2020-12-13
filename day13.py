def part1():
	earliest_time = 0
	buses = []
	with open('inputs/day13.txt') as f:
		for line in f:
			if earliest_time != 0:
				buses = line.strip("\n").replace("x,","").split(",")
				for bus in range(0,len(buses)):
					buses[bus] = int(buses[bus])
			else:
				earliest_time= int(line.strip("\n"))
	min_time = 0
	min_bus = 0
	for bus in buses:
		closest_time = bus
		while closest_time < earliest_time:
			closest_time += bus
		if min_time == 0 or (closest_time - earliest_time < min_time):
			min_time = closest_time - earliest_time 
			min_bus = bus
	print(min_time * min_bus)

# disclaimer: the three functions related to the Chinese remainder theorem
# implementation below come from the following geeks for geeks solution: 
# https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/

def extended_euclidean(a, b):
	'''
	extended_euclidean calculates x and y such that ax + by = gcd(a,b) 
	'''
	if a == 0: 
		return (b, 0, 1) 
	else: 
		g, y, x = extended_euclidean(b % a, a) 
		return (g, x - (b // a) * y, y) 
  
def modinv(a, m): 
	'''
	modinv calculates the modular multiplicative inverse of 'a' under modulo 'm'
	'''
	g, x, y = extended_euclidean(a, m) 
	return x % m 

def chinese_remainder_theorem(buses):
	'''
	chinese_remainder_theorem finds the earliest timestamp by applying the
	Chinese remainder theorem to the buses, where the relationship between the
	earliest timestamp and a bus of number n and a difference of y between the 
	timestamp of the first bus and its timestamp can be represented as:
	earliest_timestamp ≡ -y (mod n)
	This function finds earliest_timestamp that satisfies the above congruency 
	for all buses.
	'''
	mods = []
	remainders = []
	for bus in buses:
		if bus != "x":
			mods.append(int(bus))
			remainders.append((-1)*int(buses.index(bus)))
	while True:
		a = modinv(mods[1],mods[0]) * remainders[0] * mods[1] + \
		modinv(mods[0],mods[1]) * remainders[1] * mods[0] 
		mod = mods[0] * mods[1]
		remainders.remove(remainders[0]) 
		remainders.remove(remainders[0]) 
		remainders = [a % mod] + remainders
		mods.remove(mods[0]) 
		mods.remove(mods[0]) 
		mods = [mod] + mods
		if len(remainders) == 1: 
			break
	return remainders[0] 

def part2():
	buses = []
	earliest_time = 0
	with open('inputs/day13.txt') as f:
		for line in f:
			if earliest_time != 0:
				buses = line.strip("\n").split(",")
			else:
				earliest_time= int(line.strip("\n"))
	print(chinese_remainder_theorem(buses))



if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()