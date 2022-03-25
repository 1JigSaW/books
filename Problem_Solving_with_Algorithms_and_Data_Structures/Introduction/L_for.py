for item in [1,3,6,2,5]:
	print(item)

for item in range(5):
	print(item**2)

wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)