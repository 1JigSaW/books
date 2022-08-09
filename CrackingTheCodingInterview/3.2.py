class Stack:
    def __init__(self):
        self.items = []
        self.minn = None

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if len(self.items) == 0:
            self.minn = None
        elif len(self.items) == 1:
            self.minn = self.items[0]
        else:
            if item < self.minn:
                self.minn = item

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def min(self):
        return self.minn

stack = Stack()
print(stack.min())