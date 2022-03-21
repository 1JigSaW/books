S = [2,6,3,8,1]
x = 4

def double_sun(S, x):
	for i in S:
		for j in S:
			if i + j == x:
				print(i, j)

double_sun(S, x)