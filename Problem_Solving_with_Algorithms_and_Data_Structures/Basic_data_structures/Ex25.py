from timeit import Timer
from Ex18 import UnorderedList

def test_append():
    l = []
    for i in range(1000):
        l.append(i)

def test_insert():
    l = []
    for i in range(1000):
        l.insert(i, i)

def test_pop():
    l = [i for i in range(1000)]
    for i in range(len(l)):
        l.pop()

def test_remove():
    l = list(range(1000))
    for i in l:
        l.remove(i)

def test_index():
    l = list(range(1000))
    for i in l:
        l.index(i)

def test_append2():
    l = UnorderedList()
    for i in range(1000):
        l.append(i)

def test_insert2():
    l = UnorderedList()
    l.add(54)
    for i in range(1000):
        l.insert(i, 0)

def test_pop2():
    l = UnorderedList()
    for i in range(1000):
        l.add(1)
    for i in range(l.size()):
        l.pop(1)

def test_remove2():
    l = UnorderedList()
    for i in range(1000):
        l.add(1)
    for i in range(l.size()):
        l.remove(1)

def test_index2():
    l = UnorderedList()
    for i in range(1000):
        l.add(1)
    for i in range(l.size()):
        l.index(i)

t1 = Timer("test_append()", "from __main__ import test_append")
print("append ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test_insert()", "from __main__ import test_insert")
print("insert ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test_pop()", "from __main__ import test_pop")
print("pop ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test_remove()", "from __main__ import test_remove")
print("remove ",t4.timeit(number=1000), "milliseconds")
t5 = Timer("test_index()", "from __main__ import test_index")
print("index ",t5.timeit(number=1000), "milliseconds")
print("----------------------------------------------------")
t6 = Timer("test_append2()", "from __main__ import test_append2")
print("append ",t6.timeit(number=1000), "milliseconds")
t7 = Timer("test_insert2()", "from __main__ import test_insert2")
print("insert ",t7.timeit(number=1000), "milliseconds")
t8 = Timer("test_pop2()", "from __main__ import test_pop2")
print("pop ",t8.timeit(number=1000), "milliseconds")
t9 = Timer("test_remove2()", "from __main__ import test_remove2")
print("remove ",t9.timeit(number=1000), "milliseconds")
t10 = Timer("test_index2()", "from __main__ import test_index2")
print("index ",t9.timeit(number=1000), "milliseconds")