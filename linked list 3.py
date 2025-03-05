class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def__init__(self):
		self.head = None
		self.size = 0

	def insert(self, data):
		if not self.head:
			self.head = Node(data)
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = Node(data)
		self.size += 1

	def delete(self, data):
		temp = self.head
		prev = None
		while temp:
			if temp.data == data:
				if prev:
					prev.next = temp.next
				else:
					self.head = temp.next
				self.size -= 1
				break
			prev = temp
			temp = temp.next


list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
print("Size of the linked list after insertions: ", list.size) # Expected output : Size of the linked list after insertions: 3
list.delete(2)
print("Size of the linked list after deletion: ", list.size)  # Expected output: Size of the linked list after deletion: 2

