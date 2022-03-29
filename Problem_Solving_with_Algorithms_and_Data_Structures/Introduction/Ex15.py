task = [[' ', '8', ' ', '6', ' ', ' ', ' ', '7', ' '],
		['3', ' ', ' ', '1', ' ', ' ', ' ', ' ', '2'],
		[' ', ' ', '4', ' ', '3', ' ', '6', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', '6', ' ', '5', '4'],
		[' ', ' ', '8', ' ', '2', ' ', '9', ' ', ' '],
		['5', '1', ' ', '7', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', '2', ' ', '7', ' ', '4', ' ', ' '],
		['8', ' ', ' ', ' ', ' ', '3', ' ', ' ', '9'],
		[' ', '9', ' ', ' ', ' ', '5', ' ', '1', ' ']]


n = 3
for col in range(len(task) + 1):
	for k in range(len(task[0])):
		exp_arr = []
		for line in task[:n]:
			for num in line[:n]:
				if num != ' ':
					exp_arr.append(num)

		for line in task[:1]:
			for num in line:
				if num != ' ':
					exp_arr.append(num)

		for line in task:
			for num in line[:1]:
				if num != ' ':
					exp_arr.append(num)


		exp_arr = list(set(exp_arr))

		use = []
		for j in range(1,10):
			if str(j) not in exp_arr:
				use.append(j)
		print(exp_arr)
		print(use)