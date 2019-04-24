

def tow(nums, target):
	for i in range(len(nums)-1):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i,j]

print(tow([3,2,6], 8))

*****************************************************************************
最大问题：
		在range中n到m的正确写法是**range(n,m)**   yon ，
		在list中n到m的正确写法是**list(n:m)**    yon ：


