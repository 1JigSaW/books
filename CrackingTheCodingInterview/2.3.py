from linkedList import Node

def delMiddleElem(n):
	current = n
	curr = n.next
	prev = n
	count = 0
	while current:
		count += 1
		current = current.next
	if count % 2 == 0:
		return n
	mid = count // 2
	count = 0
	while curr:
		print(prev.data, curr.data)
		count += 1
		if count == mid:
			prev.next = prev.next.next 
		prev = prev.next 
		curr = curr.next
	return prev

ll = Node(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)


node = ll 
print(delMiddleElem(node))

print(node.data)
while node.next:
    node = node.next
    print(node.data)