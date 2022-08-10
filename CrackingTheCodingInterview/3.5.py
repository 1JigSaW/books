class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def sort(self):
        for passnum in range(len(self.items)-1,0,-1):
            for i in range(passnum):
                print(i)
                if self.items[i] > self.items[i+1]:
                    temp = self.items[i]
                    self.items[i] = self.items[i+1]
                    self.items[i+1] = temp

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(34)
stack.push(0)
stack.push(3123)
stack.sort()
print(stack.items)