class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None  # Extra pointer to the last node

	def add_node(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node  # set tail point to the first node
		else:
			self.tail.next = new_node
			self.tail = new_node  # update tail point to the new node

	def length_parity(self):
		# Use a flag to toggle parity: 0 for even, 1 for odd.
		parity = 0  # starting with zero elements, which is even.
		current = self.head
		while current:
			parity = 1 - parity # toggle parity
			current = current.next
		return 'Even' if parity == 0 else 'Odd'


# Test cases:

linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
print(linked_list.length_parity())  # Expected 'Odd'

linked_list = LinkedList()
linked_list.add_node(10)
linked_list.add_node(20)
linked_list.add_node(30)
linked_list.add_node(40)
print(linked_list.lenght_parity())  # Expected 'Even'

linked_list = LinkedList()
print(linked_list.length_parity())  # Expected 'Even'