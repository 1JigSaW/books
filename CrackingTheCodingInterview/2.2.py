from linkedList import Node

def search(n, item):
	current = n
	while current:
		if current.data == item:
			return current
		current = current.next
	return None


ll = Node(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

node = ll
print(search(node, 3))

print(node.data)
while node.next:
	node = node.next
	print(node.data)