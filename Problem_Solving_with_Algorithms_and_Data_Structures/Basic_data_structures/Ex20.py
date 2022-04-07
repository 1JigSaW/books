from L_list import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.tail = self.head = temp
        else:
            self.tail.setNext(temp)
            self.tail = temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def pop(self, item):
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
            current = None
        else:
            previous.setNext(current.getNext())
        self.size1 -= 1

    def insert(self, item, index):
        if index < 0 or index > self.size():
            print ("Bad Index Range!")
            return False
        curr = self.head
        prev = None
        count = 0
        node = Node(item)

        if index == self.size():
            print ("Inserting at tail")
            self.tail.next = node
            self.tail = self.tail.next
            self.size1 += 1
            return True

        while curr is not None:
            if count == index:
                break
            prev = curr
            curr = curr.next
            count += 1
        if prev is None:
            print ("Inserting at head")
            node.next = self.head
            self.head = node
        else:
            print ("Inserting in between: ", count)
            node.next = curr
            prev.next = node
        self.size1 += 1
        return True

    def index(self, item):
        current = self.head
        found = False
        ind = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                ind += 1
        return ind

    def __str__(self):
        current = self.head
        found = False
        str_list = ''
        while current != None:
            str_list += str(current.data) + ', '
            current = current.getNext()
        str_list = str_list[0: len(str_list) - 2]
        return '[' + str_list + ']'


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
print(mylist.search(93))
print(mylist.remove(93))
print(mylist.search(93))