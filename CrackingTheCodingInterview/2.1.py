from linkedList import Node
from collections import defaultdict

### O(n)
def deleteDuplicates(front):
    counted = defaultdict(bool)
    temp = front
    counted[temp.data] = True
    while (temp.next):
        # проверяем значение следующего узла
        if (counted[temp.next.data]):
            # если значение найдено в словаре, удаляем его
            temp.next = temp.next.next
        else:
            counted[temp.next.data] = True
            temp = temp.next

### O(n^2)
def deleteDuplicates_without_buf(front):
    current = front
    while current:
    	runner = current
    	while runner.next:
    		if current.data == runner.next.data:
    			runner.next = runner.next.next
    		else:
    			runner = runner.next
    	current = current.next
    return runner

ll = Node(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(1)
ll.append(4)

node = ll
print(deleteDuplicates_without_buf(node))

print(node.data)
while node.next:
    node = node.next
    print(node.data)