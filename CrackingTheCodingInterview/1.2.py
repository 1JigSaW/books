string1 = 'abc'
string2 = 'def'
string3 = 'abc'
string4 = 'cba'

def StrInStr2(text1, text2):
	if text1[::-1] == text2:
		return True
	return False

print(StrInStr2(string1, string2))
print(StrInStr2(string3, string4))

# sort

def sort(text):
	text = sorted(text)
	return text

def permutation(text1, text2):
	if (len(text1) != len(text2)):
		return False
	return sort(text1) == sort(text2)

print(permutation(string1, string2))
print(permutation(string3, string4))

