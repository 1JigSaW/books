print({3,6,"cat",4.5,False})

mySet = {3,6,"cat",4.5,False}
print(mySet)

print(len(mySet))

print(False in mySet)

print("dog" in mySet)

yourSet = {99,3,100}
print(mySet.union(yourSet))

print(mySet | yourSet)

print(mySet.intersection(yourSet))

print(mySet & yourSet)

print(mySet.difference(yourSet))

print(mySet - yourSet)

print({3,100}.issubset(yourSet))

print({3,100} <= yourSet)

print(mySet.add("house"))

mySet.remove(4.5)
print(mySet)

mySet.pop()
print(mySet)

mySet.clear()
print(mySet)
