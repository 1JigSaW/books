import timeit

d = timeit.Timer("x[10]","from __main__ import x")
d2 = timeit.Timer("x[10] = 1","from __main__ import x")

x = {j:None for j in range(1000000)}
print(d.timeit(number=1000))
print(d2.timeit(number=1000))