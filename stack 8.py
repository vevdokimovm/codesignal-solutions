class MaxStack:

	def __init__(self):
		self.stack = []
		self.max_stack = []

	def push(self, x):
		self.stack.append(x)
		# If max_stack is empty or x is greater or equal to the current max, push it onto max_stack.
		if not self.max_stack or x >= self.max_stack[-1]:
			self.max_stack.append(x)

	def pop(self):
		if not self.stack:
			return None
		popped = self.stack.pop()
		# If the popped element is the current maximum, pop it from max_stack as well.
		if self.max_stack and popped == self.max_stack[-1]:
			self.max_stack.pop()
		return popped

	def top(self):
		return self.stack[-1] if self.stack else None