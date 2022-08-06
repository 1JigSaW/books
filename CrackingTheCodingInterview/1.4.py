string1 = 'taco cat'
string2 = 'atco cta'

string3 = 'pale'
string4 = 'bake'

def checkStr(text1, text2):
	err = 0
	for i in text2:
		if i not in text1:
			err += 1
	if err == 1 or err == 0:
		return True
	return False

print(checkStr(string1, string2))
print(checkStr(string3, string4))
