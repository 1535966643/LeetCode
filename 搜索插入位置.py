

def searchInsert(nums, target):
	a = len(nums)
	if nums[0] >= target:
		a = 0
		# nums.insert(0, target)
	else:
		for i in range(len(nums)):
			if target <= nums[i]:
				a = i
				break
				# nums.insert(i, target)
	return a

	# for i in range(len(nums)):
	# 	if target <= nums[i]:
	# 		return i
	# return len(nums)

print(searchInsert([1,3,5,6],5))













