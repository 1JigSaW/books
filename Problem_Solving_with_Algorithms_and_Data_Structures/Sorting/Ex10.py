import timeit
import random

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


buble1 = timeit.Timer("bubbleSort(x)", "from __main__ import x, bubbleSort")
buble2 = timeit.Timer("bubbleSort(y)", "from __main__ import y, bubbleSort")
buble3 = timeit.Timer("bubbleSort(z)", "from __main__ import z, bubbleSort")
buble4 = timeit.Timer("bubbleSort(h)", "from __main__ import h, bubbleSort")
x = [random.randrange(0, 101) for i in range(500)]
y = [random.randrange(0, 101) for i in range(100)]
z = [random.randrange(0, 101) for i in range(1000)]
h = [random.randrange(0, 101) for i in range(1500)]
print(buble1.timeit(number=1000))
print(buble2.timeit(number=1000))
print(buble3.timeit(number=1000))
print(buble4.timeit(number=1000))