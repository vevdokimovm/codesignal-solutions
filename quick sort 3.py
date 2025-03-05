import random

def partition(arr, low, high):
	pivot = arr[low]
	i = low + 1
	j = high
	done = False
	while not done:
		# Move i to the right as long as elements are less then or equal to pivot
		while i <= j and arr[i] <= pivot:
			i += 1
		# Move j to the left as long as elements are greater than pivot
		while j >= i and arr[j] > pivot:
			j -= 1
		if j < i:
			done = True
		else:
			arr[i], arr[j] = arr[j], arr[i]
	arr[low], arr[j] = arr[j], arr[low]
	return j

def quick_sort(arr, low, high):
	if low < high:
		split_point = partition(arr, low, high)
		quick_sort(arr, low, split_point - 1)
		quick_sort(arr, split_point + 1, high)


# Generate a list of random numbers between 10 and 50
random_list = [random.randint(10, 50) for i in range(15)]

print('Original List: ', random_list)

quick_sort(random_list, 0, len(random_list) - 1)
print("List After Quick Sort: ", random_list)