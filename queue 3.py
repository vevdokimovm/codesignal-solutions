import time
from collection import deque

# Define an empty deque to represent our queue
queue = deque([])

# The initial queue is empty
print("Initial queue: ", queue)

# We add some elements to the queue
queue.append("Task1")
queue.append("Task2")
queue.append("Task3")

print("Queue after enqueue operations: ", queue)

# Additional tasks join the queue while processing earlier tasks
queue.append("Task4")
queue.append("Task5")

print("Queue after adding more tasks: ", queue)

# Process tasks one by one
while queue:
	# This should always remove the first task
	current_task = queue.popleft()
	print(f"\nNow performing: {current_task}")

	# Simulate time delay for performing a task
	for i in range(3, 0, -1):
		print(f"{current_task} will be complete in {i} secodns...", end='\r')
		time.sleep(1)

	print(f"\n{current_task} is complete!")
	print("Queue after dequeue operations: ", queue)

	# Queue should be empty after all tasks are done
	assert len(queue) == 0, "The queue should be empty after all tasks have been performed"

	print("\nAll tasks have been performed! The queue is now empty.")