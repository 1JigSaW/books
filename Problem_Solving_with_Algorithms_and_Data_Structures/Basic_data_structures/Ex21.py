from L_list import Node

class Stack:
	def __init__(self):
		self.head = None
		self.size_arr = 0

	def isEmpty(self):
		return self.size_arr == 0

	def push(self, item):
		temp = Node(item)
		temp.next = self.head
		self.head = temp
		self.size_arr += 1

	def pop(self):
		if self.head == None:
			print('Стек пуст')
		else:
			self.head = self.head.getNext()
		self.size_arr -= 1

	def size(self):
		return self.size_arr

	def __str__(self):
		if self.head != None:
			dataList = []
			curr = self.head
			while curr is not None:
				dataList.append(curr.data)
				curr = curr.next
			return dataList  
		else:
			return None


s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.isEmpty())
s.pop()
print(s.isEmpty())
s.pop()
print(s.isEmpty())
