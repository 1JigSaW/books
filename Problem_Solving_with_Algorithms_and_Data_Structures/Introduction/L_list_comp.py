sqlist = []
for x in range(1,11):
   sqlist.append(x*x)

print(sqlist)

sqlist = [x*x for x in range(1,11)]

print(sqlist)

sqlist = [x*x for x in range(1,11) if x%2 != 0]

print(sqlist)

print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou'])