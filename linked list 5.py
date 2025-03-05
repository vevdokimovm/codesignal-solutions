class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


def find_sum(head):
	stack = []
	while head:
		# implemen this
		stack.append(head.data)
		head = head.next

	sum_, index = 0, 1
	while stack:
		# implement this
		element = stack.pop()
		if index % 3 == 0:
			sum_ += element
		index += 1

	return sum_


# Example usage:
# Constructing a sample linked list: 1 -> 2
# -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
head = Node(1)
current = head
for i in range(2, 10):
	current.next = Node(i)
	current = current.next

# The reversed list is: 9, 8, 7, 6, 5, 4, 3, 2, 1
# Every third element in the reversed list:
# 7 (3rd), 4 (6th), 1 (9th)
# Sum = 7 + 4 + 1 = 12
print(find_sum(head))  # Expected output: 12