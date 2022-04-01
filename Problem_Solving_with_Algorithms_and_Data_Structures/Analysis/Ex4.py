import random

arr = [random.random()*10 for _ in range(10)]
print(arr)

# O(n)
min_el = arr[0]
for i in arr:
	if i < min_el:
		min_el = i
print(min_el)