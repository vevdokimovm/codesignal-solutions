from collections import deque

# Our queue is represented as a Python deque
issue_queue = deque()

print("Initial queue is empty:", issue_queue)

# We add some issued to the queue
issue_queue.append('Issue1')
issue_queue.append('Issue2')
issue_queue.append('Issue3')
issue_queue.append('Issue4')
issue_queue.append('Issue5')

print("Queue after enqueue operations:", issue_queue)

# We resolve issues one by one in order of their reporting
while issue_queue:
	issue = issue_queue.popleft() # This will always remove the first issue reported
	print(f'Resolving: {issue}')
	print("Queue after resolving", issue, ":", issue_queue)

# Now hte queue is again empty
assert len(issue_queue) == 0, "The queue should be empty after all issues have been resolved"
print("All issues have been resolved!")