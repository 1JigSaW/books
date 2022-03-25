myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)

myList.insert(2,4.5)
print(myList)

print(myList.pop())

print(myList)

print(myList.pop(1))

print(myList)

myList.pop(2)
print(myList)

myList.sort()
print(myList)

myList.reverse()
print(myList)

print(myList.count(6.5))

print(myList.index(4.5))

myList.remove(6.5)
print(myList)

del myList[0]
print(myList)

print((54).__add__(21))