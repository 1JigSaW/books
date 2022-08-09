from stack import Stack

class SetofStacks:

	def __init__(self, capacity):
		self.stacks = []
		self.capacity = capacity

	def push(self, item):
		if self.stacks == []:
			self.stacks.append([item])
		else:
			if len(self.stacks[-1]) >= self.capacity:
				self.stacks.append([item])
			else:
				self.stacks[-1].append(item)

	def pop(self):
		if self.stacks == []:
			print("Error")
		else:
			if len(self.stacks[-1]) == 1:
				del self.stacks[-1]
			else:
				del self.stacks[-1][-1]

	def popAt(self, index):
		if index > len(self.stacks):
			print('Error')
		del self.stacks[index][-1]

set_st = SetofStacks(4)
set_st.push(1)
set_st.push(1)
set_st.push(1)
set_st.push(1)
set_st.push(1)
set_st.push(1)
set_st.push(1)
set_st.push(1)
set_st.push(1)
print(set_st.stacks)
set_st.popAt(1)
print(set_st.stacks)