def maxLenOnes(num):
	print(bin(num))
	for i in range(len(bin(num)) - 2):
		num_n = bin(num) % 2
		print(num_n)

num = 1775
print(maxLenOnes(num))