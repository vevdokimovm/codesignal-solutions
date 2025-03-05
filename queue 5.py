from collections import deque

def interleave_queues(queue1, queue2):
	interleave_queue = deque()
	# implement this
	while queue1:
		interleave_queue.append(queue1.popleft())
		interleave_queue.append(queue2.popleft())

	return list(interleave_queue)


# Test cases 
print(interleave_queues(deque([1, 2, 3, 4, 5]), deque([6, 7, 8, 9, 10]))) # Expected output: [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
print(interleave_queue(deque([1]), deque([2]))) # Expected output: [1, 2]
print(interleave_queues(deque([1, 3, 5]), deque([2, 4, 6]))) # Expected output: [1, 2, 3, 4, 5, 6]