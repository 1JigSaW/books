def ispalindrome(word):
	word = word.lower() 
	marks = '''!()-[]{};?@#$%:'"\\,./^&amp;*_ '''
	for x in word:
		if x in marks:
			word = word.replace(x, "")  
	print(word)
	if len(word) < 2: 
		return True
	if word[0] != word[-1]: 
		return False
	return ispalindrome(word[1:-1])

print(ispalindrome('Wassamassaw'))