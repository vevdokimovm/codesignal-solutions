import random

# TODO: Implement the Quick Sort function
def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) // 2]
	# TODO: fill in the missing code
	left = [x for x in arr if x < pivot]  # elements less than 'pivot'
	middle = [x for x in arr if x == pivot]  # elements equal to 'pivot'
	right = [x for x in arr if x > pivot]  # elements larger than 'pivot'
	return quick_sort(left) + middle + quick_sort(right)


random_numbers = [random.randint(1, 50) for _ in range(15)]
print("Unsorted List: ", random_numbers)

# TODO: Use the Quick Sort function to sort the 
# list and print the sorted list
print("Sorted List: ", quick_sort(random_numbers))