# n = max(A.length, B.length)
# C[n + 1]
# c = 0
# for i = 1 to n
# 	C[i] = (A[i] + B[i] + c)
#	c = A[i] + B[i] + c/2 
# C[n + 1] = c
# return c