# O(n)

string1 = "abcdaghj"
string2 = "abcdghj"

def symbolOnString(text):
	arr = []
	for i in text:
		if i in arr:
			return True
		arr.append(i)
	return False

print(symbolOnString(string1))
print(symbolOnString(string2))


def checkDuplicates(str):
	checker = 0  
	for c in str:  
		val = ord(c) - ord('a')
		if (checker & 1<<val) > 0:
			return False
		checker |= 1<<val
	return True

print(checkDuplicates(string1))
print(checkDuplicates(string2))

