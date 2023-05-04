import sys
input = sys.stdin.readline

def dfs(matrix, visited, row, col, answer):
	if visited[row][col]: return answer
	visited[row][col] = 1
	answer += matrix[row][col]
	
	dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
	for i in range(4):	
		nextY, nextX = row + dy[i], col + dx[i]
		if 0 <= nextY < len(matrix) and 0 <= nextX < len(matrix) and not visited[nextY][nextX]: 
			answer = dfs(matrix, visited, nextY, nextX, answer)
			
	return answer
	
def solution():	
	answer = 0
	n, k = map(int, input().split(' '))
	matrix = [[0] * n for _ in range(n)]
	dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
	
	for i in range(k):
		y, x = map(int, input().split(' '))
		y -= 1
		x -= 1
		matrix[y][x] += 1
		
		for i in range(4):
			nextY, nextX = y + dy[i], x + dx[i]
			if 0 <= nextY < n and 0 <= nextX < n: matrix[nextY][nextX] += 1
			
	visited = [[0] * n for _ in range(n)]
	answer = dfs(matrix, visited, 0, 0, answer)
	
	return answer

print(solution())	