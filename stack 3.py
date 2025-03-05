class Stack:
	def __init__(self):
		self.stack = []
		self.maxSize = 10 # assuming a stack size limit for this example

	def push(self, item):
		if len(self.stack) < self.maxSize:
			self.stack.append(item)
		else:
			print("Stack Overflow. Cannot add more items")

	def pop(self):
		if len(self.stack) > 0:
			print(f"Pop element: {self.stack[-1]}")
			return self.stack.pop()
		else:
			print("Stack Underflow. Stack is empty.")
			return None # return a None value when the stack is empty

	def printStack(self):
		print(self.stack)


# create a Stack object
s = Stack()

# Push elements
for i in range(1, 4): # we deliberately try to add elements in the range 1 to 3
	print(f'Pushing Book {i} into the stack')
	s.push(i)

# Print the stack
print('Stack after pushing elements:')
s.printStack

# Pop an element
topElement = s.pop()
print(f'Popped book: Book {topElement}')

# Print the stack
print('Stack after popping an element:')
s.printStack()