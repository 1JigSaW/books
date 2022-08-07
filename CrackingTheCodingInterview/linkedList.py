class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end
