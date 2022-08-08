from linkedList import Node

def firstNode(node):
	curr = node
	prev = node
	while (curr != prev.next):
		curr = curr.next
		prev = prev.next.next
		print(curr.data, prev.data)
	return prev.data


def detectLoop(head):
 
    temp = ""
    while (head != None):
 
        if (head.next == None):
            return False

        if (head.next == temp):
            return True

        nextt = head.next
 
        head.next = temp
 
        head = nextt
 
    return False	

l1 = Node(1)
v1 = Node(2)
v2 = Node(3)
v3 = Node(4)
l1.next = v1
l1.next.next = v2
l1.next.next.next = v3
l1.next.next.next.next = v2
l1.next.next.next.next.next = v3

print(firstNode(l1))
print(detectLoop(l1))