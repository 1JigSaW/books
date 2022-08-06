matrix = [[1,0,1],
		[1,0,1],
 		[1,0,0]]
N = 3
M = 3

def clearMatrix(matrix, N, M):
	if matrix[N-1][M-1] == 1:
		return matrix
	else:
		for i in range(N):
			for j in range(M):
				if (i == N-1) or (j == M-1):
					matrix[i][j] = 0
	return matrix

print(clearMatrix(matrix, N, M))