s1 = 'waterbottle'
s2 = 'erbottlewat'

def isSubstringK(text1, text2):
	if len(text2) == len(text1):
		t1t1 = text1 + text1
		return isSubstring(t1t1, text2)
	return False