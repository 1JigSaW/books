import time
# n
def min_elem(n):
	start = time.time()
	min_var = n[0]
	for i in n:
		if i < min_var:
			min_var = i
	end = time.time()
	return min_var, end - start

n = [111, 434, 4234, 235, 32, 4, 9]
print(min_elem(n))

# n^2
def min_elem2(n):
	start = time.time()
	min_var = n[0]
	for i in n:
		for j in n:
			if i > j:
				min_var = j
	end = time.time()
	return min_var, end - start

n = [111, 434, 4234, 235, 32, 4, 9]
print(min_elem2(n))