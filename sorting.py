def insert_position(nums, target):
	low, high = 0, len(nums) - 1
	ans = len(nums)  # default insertion position at the end
	while low <= high:
		mid = (low + high) // 2
		# If the middle element is greater than or euqal to the target,
		# update ans and search the left half to find the leftmost position.
		if nums[mid] >= target:
			ans = mid
			high = mid - 1
		else:
			low = mid + 1
	return ans


# Test cases:
print(insert_position([1, 2, 3, 3, 5], 3))  # Expected output: 2
print(insert_position([1, 2, 3, 3, 5], 4))  # Expected output: 4
print(insert_position([1, 3, 5, 7, 9], 10))  # Expected output: 5