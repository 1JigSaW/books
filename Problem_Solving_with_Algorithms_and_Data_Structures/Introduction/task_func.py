import random

def rand_str(n):
	return ''.join([random.choice('qwertyuiopasdfghjklzxcvbnm ') for _ in range(n)])

def equal(rand_str, orig):
	max_o = 0
	score = 0
	max_o_str = ''
	for i in range(len(orig)):
		if rand_str[i] == orig[i]:
			score += 1
	if score == 28:
		return True
	else:
		o = round(score / 28 * 100, 2)
		if max_o < o:
			max_o = o
			max_o_str = rand_str
		return max_o, max_o_str

def activate():
	counter = 0
	while equal(rand_str(28), 'methinks it is like a weasel') != True:
		if counter % 1000 == 0:
			print(equal(rand_str(28), 'methinks it is like a weasel'))
			print(counter)
		counter += 1
	return True

print(activate())

equal(rand_str(28), 'methinks it is like a weasel')
equal('methinks it is like a weasel', 'methinks it is like a weasel')