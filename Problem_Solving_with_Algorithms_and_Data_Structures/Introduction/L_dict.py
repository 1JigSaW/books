capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals)

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])

capitals['Utah']='SaltLakeCity'
print(capitals)

capitals['California']='Sacramento'
print(len(capitals))

for k in capitals:
	print(capitals[k]," is the capital of ", k)


phoneext={'david':1410,'brad':1137}
print(phoneext)

print(phoneext.keys())

print(list(phoneext.keys()))

print(phoneext.values())

print(list(phoneext.values()))

print(phoneext.items())

print(list(phoneext.items()))

print(phoneext.get("kent"))
print(phoneext.get("kent","NO ENTRY"))
