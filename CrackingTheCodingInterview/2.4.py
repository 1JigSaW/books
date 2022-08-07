from linkedList import Node

def cutList(n, item):
	beforeStart = None
	beforeEnd = None
	afterStart = None
	afterEnd = None
	while n:
		nextt = n.next
		node.nextt = None
		if (n.data < item):
			if beforeStart == None:
				beforeStart = n
				beforeEnd = beforeStart
			else:
				beforeEnd.next = n
				beforeEnd = n
		else:
			if (afterStart == None):
				afterStart = n
				afterEnd = afterStart
			else:
				afterEnd.next = n
				afterEnd = n
				break
		n = nextt

	if beforeStart == None:
		return afterStart

	beforeEnd.next = afterStart
	return beforeStart

ll = Node(4)
ll.append(33)
ll.append(5)
ll.append(2345)
ll.append(1)

node = ll
print(cutList(node, 5))

print(node.data)
while node.next:
    node = node.next
    print(node.data)


