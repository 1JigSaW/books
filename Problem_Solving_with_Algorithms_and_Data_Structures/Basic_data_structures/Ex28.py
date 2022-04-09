from L_list import Node

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size_arr = 0 

    def isEmpty(self):
        return self.size_arr == 0 

    def enqueue(self, item):
        temp = Node(item)
        if self.front is None:
            self.front = temp
            self.back = self.front
        else:
            self.back.setNext(temp)
            self.back = self.back.getNext()
        self.size_arr += 1

    def dequeue(self):
        if self.front is None:
            print('Очередь пуста')
        else:
            self.front = self.front.getNext()
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