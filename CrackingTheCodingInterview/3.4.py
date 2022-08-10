class MyQueue:

	def __init__(self):
		self.stack_new = []
		self.stack_old = []

	def size(self):
		return len(self.stack_old) + len(self.stack_new)

	def add(self, item):
		self.stack_new.append(item)

	def __shiftStacks(self):
		if (len(self.stack_old) == 0):
			for i in self.stack_new:
				self.stack_old.append(i)

	def peek(self):
		self.__shiftStacks()
		return self.stack_old[-1]

	def remove(self):
		self.__shiftStacks();
		return self.stack_old.pop()

queue = MyQueue()

queue.add(1)
queue.add(3)
print(queue.peek())
print(queue.remove())