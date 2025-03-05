import random

def partitions(lst, low, high):
	'''
	Helper function to partition the list on the basis of pivot
	'''
	pivot = lst[high]
	idx = low - 1
	for j in range(low, high):
		if lst[j] >= pivot:
			idx += 1
			lst[idx], lst[j] = lst[j], lst[idx]
	lst[idx + 1], lst[high] = lst[high], lst[idx + 1]
	return idx + 1

def quick_sort(lst, low, high):
	'''
	Applying Quick Sort
	'''
	if len(lst) == 1:
		return lst
	if low < high:
		pi = partition(lst, low, high)
		quick_sort(lst, low, pi - 1)
		quick_sort(lst, pi + 1, high)


# Generate a list of numbers from 1 to 30
numbers = [i for i in range(1, 31)]

# Print the original list
print("Original List:", numbers)

# Use Quick Sort on the list
quick_sort(numbers, 0, len(numbers) - 1)

# Print the sorted list
print("Sorted List:", numbers)