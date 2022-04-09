class Node:

    def __init__(self, data):
        self.data = data
        self.front = None
        self.back = None

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.size_list = 0

    def __str__(self):
        str_list = []
        curr = self.head
        for _ in range(self.size_list):
            str_list.append(curr.data)
            curr = curr.front
        return f'{str_list}'

    def size(self):
        return self.size_list

    def isEmpty(self):
        return self.size_list == 0

    def addFront(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            node.front = node
            node.back = node
        else:
            node.front = self.head
            node.back = self.head.back
            self.head.back.front = node
            self.head.back = node
            self.head = node
            self.size_list += 1

    def addBack(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            node.front = node
            node.back = node
        else:
            node.back = self.head.back
            node.front = self.head
            self.head.back.front = node
            self.head.back = node
            self.size_list += 1

    def removeFront(self):
        if self.isEmpty():
            print('Список пуст')
        else:
            node = self.head
            self.head.front.back = self.head.back
            self.head.back.front = self.head.front
            self.head = self.head.front
            node.front = None
            node.back = None
            self.size_list -= 1

    def removeBack(self):
        if self.isEmpty:
            print('Список пуст')
        else:
            node = self.head.back
            self.head.back.back.front = self.head
            self.head.back = self.head.back.back
            node.front = None
            node.back = None
            self.size_list -= 1

    def search(self, item):
        if self.isEmpty():
            print('Список пуст')
        else:
            ind = 0
            curr = self.head
            found = False
            while ind != self.size_list:
                if curr.data == item:
                    found = True
                    break
                ind += 1
            if found:
                return ind
            return f'Объект не найден'

    def insert(self, data, index):
        if self.isEmpty():
            print('Список пуст')
        else:
            if index < 0 or index > self.size_list:
                print("Неккоректный индекс")
            else:
                node = Node(data)

                if self.head is None:
                    self.head = node
                    self.head.front = self.head
                    self.head.back = self.head
                else:
                    count = 0
                    curr = self.head
                    while (count < index-1):
                        curr = curr.front
                        count += 1
                    node.back = curr
                    node.front = curr.front
                    curr.front.back = node
                    curr.front = node
                    if index == 0:
                        self.head = node
                    self.size_list += 1


item = DoubleLinkedList()
print(item)
item.addFront(1)
print(item)
item.addBack(2)
print(item)
item.removeFront()
print(item)