string1 = "Mr John Smith"

def spacePut(text):
	newStr = ''
	for i in text:
		if i == ' ':
			newStr += '%20'
		else:
			newStr += i
	return newStr

def urlize(a, true_len):
    ei = true_len - 1

    nr_spaces = 0
    for i in range(true_len):
        if a[i] == " ":
            nr_spaces += 1

    ei = true_len - 1 - (nr_spaces//3) * 2
    print(ei)
    # print(f"Turns out the string starts at {ei}")
    end_i = true_len-1
    while ei >= 0:
        # print(f"Not at {ei} and outputloc {end_i}")
        if a[ei] != " ":
            a[end_i] = a[ei]
        else:
            a[end_i] = "0"
            a[end_i-1] = "2"
            a[end_i-2] = "%"
            end_i -= 2
        end_i -= 1
        ei -= 1
    return "".join(a)

print(spacePut(string1))
print(urlize(['a', 'b', 'c', ' ', 'd', ' ', ' '], 7))

# book
def replaceSpaces(text, length):
    count = 0
    text = list(text)
    for i in range(length):
        if text[i] == ' ':
            count += 1

    new_length = length + count * 2
    text.append('\0')
    for i in range(length-1):
        if text[i] == ' ':
            text[i] = '\0';
    return "".join(text)

print(replaceSpaces(string1, 13))
