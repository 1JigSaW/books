from linkedList import Node

def polindrome(node):
	head = node
	arr = []
	count = 0
	while node:
		count += 1
		node = node.next
	iterator = 0
	if count % 2 == 0:
		while head:
			if count // 2 >= iterator+1:
				arr.append(head.data)
				head = head.next
				iterator += 1
			else:
				for i in arr[::-1]:
					if head.data != i:
						return False
					head = head.next
	else:
		while head:
			if count // 2 >= iterator+1:
				arr.append(head.data)
				head = head.next
				iterator += 1
			else:
				head = head.next
				for i in arr[::-1]:
					print(i, head.data)
					if head.data != i:
						return False
					head = head.next
	return True 

def isPalindrome(node):
	fast = node
	slow = node

	stack = []

	while (fast != None and fast.next != None):
		stack.append(slow.data)
		slow = slow.next
		fast = fast.next.next

	print(stack)

	if (fast != None):
		slow = slow.next

	while (slow != None):
		top = stack.pop()
		print(top, slow.data)
		if (top != slow.data):
			return False
		slow = slow.next
	return True




l1 = Node(0)
l1.append(1)
l1.append(2)
l1.append(1)
l1.append(0)

print(polindrome(l1))
print(isPalindrome(l1))

