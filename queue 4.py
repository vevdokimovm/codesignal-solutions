from collections import deque

# Our queue is represented as a deque
catering_queue = deque()

print("Initial queue is empty:", catering_queue)

# We add some orders to the queue by using append method
catering_queue.append('Order1')
catering_queue.append('Order2')
catering_queue.append('Order3')
catering_queue.append('Order4')
catering_queue.append('Order5')
catering_queue.append('Order6')

print("Queue after enqueue operations:", catering_queue)

# We process orders one by one in order of their arrival by using popleft method
while catering_queue: # TODO: replace False with a proper check:
	order = catering_queue.popleft()
	print(f'Processing: {order}')
	print("Queue after processing", order, ":", catering_queue)