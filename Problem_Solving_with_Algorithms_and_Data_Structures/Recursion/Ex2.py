def reverseList(n):
	if len(n) == 1:
		return n
	else:
		return reverseList(n[1:]) + [n[0]] 

print(reverseList([1,2,3,4,5]))