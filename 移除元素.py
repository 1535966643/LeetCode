
# .remove()	# 删除指定元素   但是只是删除第一个元素
# .pop() 		# 删除指定位置元素

def aa(nums, val):
	# for x in nums:
	# 	print(x)
	# 	if x == val:
	# 		nums.remove(x)
	# 		# print(nums)
			
	# return len(nums)
	while val in nums:
		print(nums)
		nums.remove(val)
	return len(nums)
aa([3,2,2,3], 2)
# print()

# *********************************************
# 这边的while 和 for是有很大区别   




