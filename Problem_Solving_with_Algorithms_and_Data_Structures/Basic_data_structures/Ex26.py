from Ex22 import Queue
from Ex21 import Stack
import timeit

pop_stack = timeit.Timer("x.pop()", 
	"from __main__ import x")
push_stack = timeit.Timer("x.push(300)", 
	"from __main__ import x")
size_stack = timeit.Timer("x.size()", 
	"from __main__ import x")

dequeue_queue = timeit.Timer("y.dequeue()", 
	"from __main__ import y")
enqueue_queue = timeit.Timer("y.enqueue(33)", 
	"from __main__ import y")
size_queue = timeit.Timer("y.size()", 
	"from __main__ import y")

x = Stack()
for i in range(10000000):
	x.push(33)
y = Queue()
for i in range(10000000):
	y.enqueue(33)
print(pop_stack.timeit(number=1000))
print(push_stack.timeit(number=1000))
print(size_stack.timeit(number=1000))
print()
print(dequeue_queue.timeit(number=1000))
print(enqueue_queue.timeit(number=1000))
print(size_queue.timeit(number=1000))