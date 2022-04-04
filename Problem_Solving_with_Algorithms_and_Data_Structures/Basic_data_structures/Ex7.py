from L_list import Node

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        temp = Node()
        if self.front == None:
            self.back = self.front = temp
        else:
            self.back.setNext(temp)
            self.front = self.back.setNext()


    def dequeue(self):
        temp = self.front
        if self.front.getNext() is None:
            self.front = None
            self.back = None
        else:
            self.front = self.front.getNext()
        return temp

    def size(self):
        return len(self.items)
