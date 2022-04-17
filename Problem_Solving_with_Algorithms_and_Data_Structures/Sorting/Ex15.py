import timeit
import random


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    piv = sorted([first, last, ((first + last) // 2)])[1]
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

quick1 = timeit.Timer("quickSort(x)", "from __main__ import x, quickSort")
quick2 = timeit.Timer("quickSort(y)", "from __main__ import y, quickSort")
quick3 = timeit.Timer("quickSort(z)", "from __main__ import z, quickSort")
quick4 = timeit.Timer("quickSort(h)", "from __main__ import h, quickSort")
x = [random.randrange(0, 101) for i in range(50)]
y = [random.randrange(0, 101) for i in range(100)]
z = [random.randrange(0, 101) for i in range(500)]
h = [random.randrange(0, 101) for i in range(1000)]
print(quick1.timeit(number=1000))
print(quick2.timeit(number=1000))
print(quick3.timeit(number=1000))
print(quick4.timeit(number=1000))