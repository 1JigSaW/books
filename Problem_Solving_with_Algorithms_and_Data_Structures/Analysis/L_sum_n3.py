import time

def sumOfN3(n):
   start = time.time()
   res = (n*(n+1))/2
   end = time.time()
   return res, end-start

print(sumOfN3(10))

for i in range(5):
   print(f"Sum is {sumOfN3(1000)[0]} required {sumOfN3(1000)[1]} seconds")

for i in range(5):
   print(f"Sum is {sumOfN3(10000)[0]} required {sumOfN3(10000)[1]} seconds")

for i in range(5):
   print(f"Sum is {sumOfN3(100000)[0]} required {sumOfN3(100000)[1]} seconds")

for i in range(5):
   print(f"Sum is {sumOfN3(1000000)[0]} required {sumOfN3(1000000)[1]} seconds")
