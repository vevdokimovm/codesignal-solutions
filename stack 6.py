def string_end(string, n):
	stack = list(string)
	result = ''
	# implement this
	while len(stack):
		result += stack.pop()
	return result[:n]


print(string_end("ijkshgegassem tnatropmi", 17)) # Expected output: important message
print(string_end("ffsfatad", 4)) # Expected output: data
print(string_end("IA", 2)) # Expected output: AI