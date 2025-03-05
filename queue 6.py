from collections import deque

class MovingAverage:
	def __init__(self, size):
		self.queue = deque() # Initialize deque instance
		self.size = size
		self.total = 0

	def calculate_moving_average(self, word):
		# If the queue is full, remove the oldest word and adjust the total.
		if len(self.queue) == self.size:
			removed_word = self.queue.popleft()
			self.total -= len(removed_word)
		# Add the new word and update the total.
		self.queue.append(word)
		self.total += len(word)
		# Calculate and return the moving average rounded to 2 decimal places.
		return round(self.total / len(self.queue), 2)


# Test samples
ma = MovingAverage(3)
print(ma.calculate_moving_average('one')) # Expected: 3.0
print(ma.calculate_moving_average('two')) # Expected: 3.0
print(ma.calculate_moving_average('three')) # Expected: 3.67
print(ma.calculate_moving_average('four')) # Expected: 4.0
print(ma.calculate_moving_average('five')) # Expected: 4.33
print(ma.calculate_moving_average('six')) # Expected: 3.67