def part1():
	valid_passwords = 0
	with open('inputs/day2.txt') as f:
	    for line in f:
	    	line = line.strip('\n')
	    	lowerRange = int(line.split('-')[0])
	    	upperRange = int(line.split('-')[1].split(' ')[0])
	    	letter = line.split('-')[1].split(' ')[1].strip(':')
	    	word = line.split('-')[1].split(' ')[2]
	    	if word.count(letter) >= lowerRange and word.count(letter) <= upperRange:
	    		valid_passwords += 1
	f.close()
	print("Valid passwords:", str(valid_passwords))

def part2():
	valid_passwords = 0
	with open('inputs/day2.txt') as f:
	    for line in f:
	    	line = line.strip('\n')
	    	first_position = int(line.split('-')[0])
	    	second_position = int(line.split('-')[1].split(' ')[0])
	    	letter = line.split('-')[1].split(' ')[1].strip(':')
	    	word = line.split('-')[1].split(' ')[2]
	    	first_ok = False
	    	second_ok = False
	    	if first_position <= len(word):
	    		if word[first_position - 1] == letter:
	    			first_ok = True
	    	if second_position <= len(word):
	    		if word[second_position - 1] == letter:
	    			second_ok = True
	    	if first_ok and second_ok:
	    		continue
	    	elif first_ok or second_ok:
	    		valid_passwords += 1
	f.close()
	print("Valid passwords:", str(valid_passwords))

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()

