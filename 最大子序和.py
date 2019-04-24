

def zixu(nums):
	finds = 0
	s = 0
	t = 0

	for i in range(len(nums)):
		if s > 0:
			s += nums[i]
		else:
			s = nums[i]
		if s > finds:
			finds = s
		if nums[i] < 0:
			t = t+1

	if t == len(nums):
		finds = max(nums)
	return finds 

print(zixu([3,2,-3,-1,1,-3,1,-1]))




















