class Stack:
	def __init__(self):
		self.stack = []
		self.maxSize = 10

	def push(self, item):
		if len(self.stack) < self.maxSize:
			self.stack.append(item)
			print(f'Pushed {item} to the stack')
		else:
			raise Exception('Stack Overflow. Cannot push \
							 more items to the stack.')

	def pop(self):
		if len(self.stack) > 0:
			popped_element = self.stack.pop()
			print(f'Popped element: {popped_element}')
			return popped_element
		else:
			raise Exception('Stack Underflow. The stack is empty.')

	# TODO: Implement a method to peek the top element of the stack
	# remember, you just have to look at the top element, not remove it
	def peek(self):
		if len(self.stack) > 0:
			print(f'The last element in the stack is {self.stack[-1]}')
		else:
			print('There are no elements in the stack')

	def is_empty(self):
		return len(self.stack) == 0

	def get_size(self):
		return len(self.stack)


my_stack = Stack()
for i in range(1, 7):
	my_stack.push(i)

# TODO: Call the peek function to view the top element of the stack
my_stack.peek()
print("\nOperations after attempting to pop the top element:")
my_stack.pop()

# TODO: Again, call the peek function to view the new top element of the stack
my_stack.peek()
stack_size = my_stack.get_size()
print("\nOperations when attempting to pop all elements:")
for _ in range(stack_size):
	my_stack.pop()

# TODO: Try to peek into an empty stack
my_stack.peek()
if my_stack.is_empty():
	print("The stack is empty.")
else:
	print("The stack is not empty.")