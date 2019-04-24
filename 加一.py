

def jiayi(nums):
	t = len(nums)
	s = 0
	for i in range(t):
		t -= 1
		s += nums[i] * (10**t)
	s += 1
	t = len(str(s))
	numss=[]
	for j in range(t):
		t -= 1
		print(j)
		numss.append(int(s)//int(10**t))
		s = s % (10**t)
	return numss

print(jiayi([9])) 
