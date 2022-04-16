import timeit
import random

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

def defaultSearch(alist, item):
    for i in alist:
        if i == item:
            return True
    return False

binary = timeit.Timer("binarySearch(x, x[9988])", "from __main__ import x, binarySearch")

default = timeit.Timer("defaultSearch(x, x[9988])", "from __main__ import x, defaultSearch")

x = [random.random() for i in range(100000)]
print(binary.timeit(number=1000))
print(default.timeit(number=1000))