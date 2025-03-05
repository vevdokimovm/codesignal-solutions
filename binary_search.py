# Implementation of Binary Search on a specific use case

# List of sorted products' prices in an e-commerce company
products_price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 
65, 70, 75, 80, 85, 90, 95]

def binary_search_iterative(data, target):
	low = 0
	high = len(data)
	while high - low > 1:
		mid = (low + high) // 2
		if target < data[mid]:
			high = mid
		elif target > data[mid]:
			low = mid
		else: # if target is euqal to data[mid]
			return mid
	return low if data[low] == target else None

def search_price(customer_query):
	result = binary_search_iterative(products_price, customer_query)
	if result is not None:
		print(f"Product of price ${customer_query} is found at position {result} in the price list.")
	else:
		print(f"No product is found with price ${customer_query}.")


# Searching for a price that exists
search_price(30)

# Searching for a price that doesn't exist
search_price(31)