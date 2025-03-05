def evaluate_postfix_inverse(expression):
	# implement this
	stack = []
	for element in expression.split(' '):
		if element.isdigit():
			stack.append(int(element))
		else:
			operand1 = stack.pop()
			operand2 = stack.pop()

			if element == '+': stack.append(operand1 + operand2)
			elif element == '-': stack.append(operand1 - operand2)
			elif element == '*': stack.append(operand1 * operand2)
			elif element == '/': stack.append(operand1 / operand2)

	return stack[0]


print(evaluate_postfix_inverse("2 3 -")) # Expected output: 1
print(evaluate_postfix_inverse("2 3 +")) # Expected output: 5
print(evaluate_postfix_inverse("6 3 *")) # Expected output: 18