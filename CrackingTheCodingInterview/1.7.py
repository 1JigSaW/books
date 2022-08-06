matrix = [[1,0,1],
		[1,0,1],
 		[1,0,1]]
N = 3

def rotate(matrix, N):
	for layer in range(N//2):
		first = layer
		last = N - 1 - layer
		for i in range(last):
			offset = i - first
			top = matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] = matrix[last][last-offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = top
	return matrix

print(rotate(matrix, N))