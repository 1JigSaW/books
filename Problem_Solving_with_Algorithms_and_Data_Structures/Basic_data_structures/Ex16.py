from L_list import Node


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size1 = 0

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        # temp = Node(item)
        # temp.setNext(self.head)
        # self.head = temp
        temp = Node(item)
        if self.head == None:
            self.tail = self.head = temp
        else:
            temp.setNext(self.head)
            self.head = temp
        self.size1 += 1

    def size(self):
        return self.size1

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.size1 -= 1

    def append(self, item):
        # current = self.head
        # prev = None
        # while current != None:
        #     prev = current
        #     current = current.getNext()
        # temp = prev.setNext(Node(item))
        # current = temp
        temp = Node(item)
        if self.head == None:
            self.tail = self.head = temp
        else:
            self.tail.setNext(temp)
            self.tail = temp
        self.size1 += 1

    def __str__(self):
        current = self.head
        found = False
        str_list = ''
        while current != None:
            str_list += str(current.data) + ', '
            current = current.getNext()
        str_list = str_list[0: len(str_list) - 2]
        return '[' + str_list + ']'


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
mylist.append(544)
print(mylist.size())
print(mylist.search(544))
print(mylist.tail)
#mylist.remove(345435)
print(mylist)