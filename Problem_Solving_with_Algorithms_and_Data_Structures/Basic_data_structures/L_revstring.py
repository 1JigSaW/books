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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'{self.items}'

def revstring(mystr):
    old_arr = Stack()
    for i in mystr:
        old_arr.push(i)
    new_arr = Stack()
    while not old_arr.isEmpty():
        new_arr.push(old_arr.peek())
        old_arr.pop()
    return new_arr


print(revstring('apple'))
