from linkedList import Node

def intersection(node1, node2):
	p1, p2 = node1, node2
	while p1 != p2:
		p1 = node2 if not p1 else p1.next
		p2 = node1 if not p2 else p2.next
	return p1

newNode = Node(10)
head1 = newNode
newNode = Node(3)
head2 = newNode
newNode = Node(6)
head2.next = newNode
newNode = Node(9)
head2.next.next = newNode
newNode = Node(15)
head1.next = newNode
head2.next.next.next = newNode
newNode = Node(30)
head1.next.next = newNode

print(intersection(head1, head2))