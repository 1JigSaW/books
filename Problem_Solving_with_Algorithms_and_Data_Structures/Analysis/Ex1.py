import timeit

popzero = timeit.Timer("x[10]",
                       "from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number=1000))