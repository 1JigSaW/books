string1 = 'abccba'

def polindrome(text):
	d = {}
	for i in range(len(text)):
		if text[i] not in d:
			d[text[i]] = 1
		else:
			d[text[i]] += 1
	print(d)
	if len(d) == 0:
		return True
	return False

print(polindrome(string1))

##############
from collections import Counter

def anagramCheck(text1, text2):
	d1 = {}
	for i in text1:
		if i not in d1 and i != ' ':
			d1[i] = 1
		elif i != ' ':
			d1[i] += 1
	d2 = {}
	for i in text2:
		if i not in d2 and i != ' ':
			d2[i] = 1
		elif i != ' ':
			d2[i] += 1
	return d1 == d2

print(anagramCheck(string1, string2))