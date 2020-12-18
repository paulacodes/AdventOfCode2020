def part1():
	expressions = []
	sum = 0
	with open('inputs/day18.txt') as f:
		for expression in f:
			expression = list(expression.strip("\n"))
			stack =[]
			postfix = ""
			for i in range(len(expression)):
				if expression[i].isdigit():
					postfix += expression[i]
				elif expression[i] == "(":
					stack.append(expression[i])
				elif expression[i] == ")":
					while stack and stack[-1] != "(":
						postfix += stack.pop()
					stack.pop()
				elif expression[i] in ["+", "*"]:
					if not stack or stack[-1] == "(":
						stack.append(expression[i])
					else:
						while stack and stack[-1] != "(":
							postfix += stack.pop()
						stack.append(expression[i])
			while stack:
				postfix += stack.pop()
			for i in range(len(postfix)):
				if postfix[i].isdigit():
					stack.append(int(postfix[i]))
				elif postfix[i] == "+":
					a = int(stack.pop())
					b = int(stack.pop())
					a += b
					stack.append(a)
				elif postfix[i] == "*":
					a = int(stack.pop())
					b = int(stack.pop())
					a *= b
					stack.append(a)
			sum += stack.pop()
	print(sum)

def part2():
	expressions = []
	sum = 0
	precedence = { 
		"+": 1,
		"*": 0
	}
	with open('inputs/day18.txt') as f:
		for expression in f:
			expression = list(expression.strip("\n"))
			stack =[]
			postfix = ""
			for i in range(len(expression)):
				if expression[i].isdigit():
					postfix += expression[i]
				elif expression[i] == "(":
					stack.append(expression[i])
				elif expression[i] == ")":
					while stack and stack[-1] != "(":
						postfix += stack.pop()
					stack.pop()
				elif expression[i] in ["+", "*"]:
					if not stack or stack[-1] == "(":
						stack.append(expression[i])
					else:
						while stack and stack[-1] != "(" \
						and precedence[expression[i]] <= precedence[stack[-1]]:
							postfix += stack.pop()
						stack.append(expression[i])
			while stack:
				postfix += stack.pop()
			for i in range(len(postfix)):
				if postfix[i].isdigit():
					stack.append(int(postfix[i]))
				elif postfix[i] == "+":
					a = int(stack.pop())
					b = int(stack.pop())
					a += b
					stack.append(a)
				elif postfix[i] == "*":
					a = int(stack.pop())
					b = int(stack.pop())
					a *= b
					stack.append(a)
			sum += stack.pop()
	print(sum)


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()

