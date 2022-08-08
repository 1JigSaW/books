from linkedList import Node

def mergeIntSum(node1, node2):
    string1 = ''
    while node1:
        string1 += str(node1.data)
        node1 = node1.next
    string1 = string1[::-1]
    string2 = ''
    while node2:
        string2 +=  str(node2.data)
        node2 = node2.next
    string2 = string2[::-1]
    res = str(int(string1) + int(string2))
    res = list(res)
    print(res)
    new_list = Node(res[0])
    for i in res[1:]:
        new_list.append(int(i))
    return new_list

def addTwoNumbers(l1, l2):
    head = None
    temp = None
    carry = 0
    while l1 is not None or l2 is not None:
        sum_value = carry

        if l1 is not None:
            sum_value += l1.data
            l1 = l1.next

        if l2 is not None:
            sum_value += l2.data
            l2 = l2.next

        node = Node(sum_value % 10)
        
        carry = sum_value // 10

        if temp is None:
            temp = head = node

        else:
            temp.next = node
            temp = temp.next

    if carry > 0:
        temp.next = Node(carry)
    return head

l1 = Node(7)
l1.append(1)
l1.append(6)

l2 = Node(5)
l2.append(9)
l2.append(2)

l3 = addTwoNumbers(l1, l2)
print(l3.data)
while l3.next:
    l3 = l3.next
    print(l3.data)
