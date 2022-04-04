class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
        self.items.append(item)


    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()
print(queue.enqueue(2))
print(queue.enqueue(4))
print(queue.size())