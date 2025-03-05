import random

def partition_desc(arr, low, high):
	# Choose the first element as pivot
	pivot = arr[low]
	i = low + 1
	j = high
	while True:
		# Move i rightwards while elements are greater than or equal to pivot (for descending order)
		while i <= j and arr[i] >= pivot:
			i += 1
		# Move j leftwards while elements are less than pivot
		while i <= j and arr[j] < pivot:
			j -= 1
		# If pointers cross, we've partitioned the array
		if j < i:
			break
		# Otherwise, swap the elements at i and j
		arr[i], arr[j] = arr[j], arr[i]
	# Place the pivot in its correct position
	arr[low], arr[j] = arr[j], arr[low]
	return j

def quick_sort_desc(arr, low, high):
	if low < high:
		# Partititon the array and get the pivot index
		pivot_index = partition_desc(arr, low, high)
		# Recursively apply quick sort to the left and right subarrays
		quick_sort_desc(arr, low, pivot_index - 1)
		quick_sort_desc(arr, pivot_index + 1, high)


# Generate a list of 20 random numbers between 50 and 100
random_numbers = [random.randint(50, 100) for _ in range(20)]
print("Unsorted List: ", random_numbers)

# Sort the list in descending order using Quick Sort
quick_sort_desc(random_numbers, 0, len(random_numbers) - 1)
print("Sorted in Descending Order: ", random_numbers)