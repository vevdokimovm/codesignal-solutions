def are_brackets_balanced(s):
	brackets = set(['(', ')', '[', ']', '{', '}'])
	bracket_map = {'(': ')', '[': ']', '{': '}'}
	open_brackets = set(['(', '[', '{'])
	stack = []
	# implement this
	for character in s:
		if character not in brackets:
			# Skipping non-bracket characters
			continue
		if character in open_brackets:
			stack.append(character)
		elif stack and character == bracket_map[stack[-1]]:
			stack.pop()
		else:
			return False
	return len(stack) == 0


print(are_brackets_balanced('(abc[d]{fg})')) # Expected output: True
print(are_brackets_balanced('(a[bcd{fg}h]i)')) # Expected output: True
print(are_brackets_balanced("(abc{d[fg]h)i")) # Expected output: False
print(are_brackets_balanced("({a[bcd]})")) # Expected output: True