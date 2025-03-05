from collections import deque

# Our queue is represented as a Python collections deque
queue = deque()

print("Initial queue is empty:", queue)

# We add some elements to the queue
queue.append('Task1')
queue.append('Task2')
queue.append('Task3')
print('Queue after enqueue operations:', queue)

# We perform tasks one by one in order of addition to the queue
while queue:
	task = queue.popleft()  # This should always remove the first task
	print(f'Performing: {task}')
	print("Queue after removing", task, ":", queue)

# Now the queue is again empty
assert not queue, "The queue should be empty after all tasks have been performed"
print("All tasks have been performed!")