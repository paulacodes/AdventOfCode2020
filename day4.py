def check_validity(passport):
	"""
	check_validity checks is a passport is valid or not, returning True if it is and False if not
	:param passport: the string representation of a passport
	"""
	data = {}
	valid = True
	if "byr:" not in passport or "iyr:" not in passport or "eyr:" not in passport or "hgt:" not in passport or "hcl:" not in passport or "ecl:" not in passport or "pid:" not in passport:
		return False
	for pair in (passport.split(" ")):
		if ":" in pair:
			pair = pair.split(":")
			data[pair[0]] = pair[1]
	if not data['byr'].isnumeric() or not data['iyr'].isnumeric() or not data['eyr'].isnumeric():
		return False
	if int(data['byr']) < 1920 or int(data['byr']) > 2002:
		return False
	if int(data['iyr']) < 2010 or int(data['iyr']) > 2020:
		return False
	if int(data['eyr']) < 2020 or int(data['eyr']) > 2030:
		return False
	if "cm" in data['hgt']:
		number = data['hgt'].split('cm')[0]
		if not number.isnumeric():
			return False
		else:
			if int(number) < 150 or int(number) > 193:
				return False
	elif 'in' in data['hgt']:
		number = data['hgt'].split('in')[0]
		if not number.isnumeric():
			return False
		else:
			if int(number) < 59 or int(number) > 76:
				return False
	else:
		return False
	if data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False
	if not data['pid'].isnumeric() or len(data['pid']) is not 9:
		return False
	valid_hcl = "0123456789abcdef"
	if data['hcl'][0] is not "#":
		return False
	else: 
		if len(data['hcl']) != 7:
			return False
		else:
			for char in data['hcl'][1:7]:
				if char not in valid_hcl:
					return False
	return True

def part1():
	passport = ""
	valid_passports = 0
	with open('inputs/day4.txt') as f:
		for line in f:
			if line != "\n":
				passport += line.strip("\n") + " "
			else:
				if "byr:" in passport and "iyr:" in passport and "eyr:" in passport and "hgt:" in passport and "hcl:" in passport and "ecl:" in passport and "pid:" in passport:
					valid_passports += 1
				passport = ""
		if "byr:" in passport and "iyr:" in passport and "eyr:" in passport and "hgt:" in passport and "hcl:" in passport and "ecl:" in passport and "pid:" in passport:
			valid_passports += 1
	f.close()
	print("Valid passports", str(valid_passports))

def part2():
	passport = ""
	valid_passports = 0
	with open('inputs/day4.txt') as f:
		for line in f:
			if line != "\n":
				passport += line.strip("\n") + " "
			else:
				if check_validity(passport):
					valid_passports += 1
				passport = ""
		if check_validity(passport):
			valid_passports += 1
	f.close()
	print("Valid passports", str(valid_passports))


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()
