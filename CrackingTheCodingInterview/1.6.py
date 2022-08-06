string = 'aaabbbccccca'


### O(p + k^2) 

def compression(text):
	if len(set(text)) == len(text):
		return text
	counter = 0
	new_str = ''
	for i in range(len(text)):
		if text[i] == text[i-1]:
			counter += 1
		else:
			new_str += text[i-1] + str(counter)
			counter = 1
	new_str += text[i] + str(counter)
	return new_str

print(compression(string))