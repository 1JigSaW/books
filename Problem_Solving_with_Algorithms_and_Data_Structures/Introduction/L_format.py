print("Hello")

print("Hello","World")

print("Hello","World", sep="***")

print("Hello","World", end="***")

aName = 'JigSaW'
age = 2
print(aName, "is", age, "years old.")

print("%s is %d years old." % (aName, age))

price = 24
item = "banana"
print("The %s costs %d cents" % (item, price))

print("The %+10s costs %5.2f cents" % (item, price))

print("The %+10s costs %10.2f cents" % (item, price))

itemdict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents" % itemdict)
