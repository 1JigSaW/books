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

def binarySearchRec(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearchRec([alist[i] for i in range(midpoint)],item)
            else:
                return binarySearchRec([alist[i] for i in range(midpoint, midpoint + midpoint)], item)


binary = timeit.Timer("binarySearch(x, x[9988])", "from __main__ import x, binarySearch")

binaryRec = timeit.Timer("binarySearchRec(x, x[9988])", "from __main__ import x, binarySearchRec")

x = [random.random() for i in range(100000)]
print(binary.timeit(number=1000))
print(binaryRec.timeit(number=1000))