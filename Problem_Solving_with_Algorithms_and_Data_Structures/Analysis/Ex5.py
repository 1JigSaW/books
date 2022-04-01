import random

arr = [random.random()*10 for _ in range(10)]
print(arr)

# O(n)
sort_arr = sorted(arr)
print(sort_arr[0])