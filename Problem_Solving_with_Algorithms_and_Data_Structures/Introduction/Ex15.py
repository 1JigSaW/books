task = [[' ', '8', ' '],
		['3', ' ', ' '],
		[' ', ' ', '4']]


arr = []
for col in range(len(task)):
	for k in range(len(task[0])):
		exp_arr = []
		use = []
		if task[col][k] == ' ':

			for line in task[col:col+1]:
				for num in line:
					if num != ' ':
						exp_arr.append(num)


			for line in task:
				for num in line[k:k+1]:
					if num != ' ':
						exp_arr.append(num)



			exp_arr = list(set(exp_arr))

			for j in range(1,10):
				if str(j) not in exp_arr:
					use.append(j)
			print(use)
			
			arr.append(use)
		else:
			arr.append(use)
print(arr)

k = 0
for i in range(len(task)):
	for j in range(len(task[i])):
		if task[i][j] == ' ':
			task[i][j] = arr[k][0]
			k += 1

print(len(task))
