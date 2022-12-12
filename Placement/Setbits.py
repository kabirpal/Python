def largestNum(n):
	num = 0
	for i in range(32):
		x = 1 << i
		if (x - 1) <= n:
			num = (1 << i) - 1
		else:
			break
	return num
    
if __name__ == "__main__":
	N = 8
	print(largestNum(N))
