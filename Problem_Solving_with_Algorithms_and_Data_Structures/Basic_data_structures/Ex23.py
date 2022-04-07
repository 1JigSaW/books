from L_list import Node

class Deque:
	def __init__(self):
		self.front = None
		self.back = None
		self.size_arr = 0

	def isEmpty(self):
		return self.size_arr == 0

	def addFront(self, item):
		temp = Node(item)
		if self.front is None:
			self.front = temp
		else:
			temp.setNext(self.front)
			self.front = temp
		self.size_arr += 1

	def addBack(self, item):
		temp = Node(item)
		if self.back is None:
			self.front.setNext(self.back)
			self.back = temp
		else:
			self.back.setNext(temp)
			self.back = self.back.getNext()
		self.size_arr += 1

	def removeFront(self):
		if self.front is None:
			print('Дек пуст')
		else:
			self.front.setNext(self.front.getNext())
			self.front = self.front.getNext()
		self.size_arr -= 1

	def removeBack(self):
		self.size_arr -= 1

	def size(self):
		return self.size_arr

	def __str__(self):
		current = self.front
		arr = []
		while current is not None:
			arr.append(current.getData())
			current = current.getNext()
		return f'{arr}'

d = Deque()
print(d.isEmpty())
d.addFront(4)
print(d.isEmpty())
d.addFront(5)
print(d.isEmpty())
print(d)
d.removeFront()
d.removeFront()
d.removeFront()
print(d)
d.addFront(4)
print(d.isEmpty())
d.addFront(5)
print(d)
d.addBack(6)
print(d)