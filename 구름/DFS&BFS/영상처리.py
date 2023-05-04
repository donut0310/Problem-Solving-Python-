from collections import deque
import sys

input = sys.stdin.readline

def solution():
	answer = [0, 0]
	m, n = map(int, input().split(' '))
	matrix = []
	visited = [[0] * m for i in range(n)]
	
	for i in range(n):
		matrix.append(input().rstrip())

	dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
	
	for i in range(n):
		for j in range(m):
			if matrix[i][j] == '#' and not visited[i][j]:
				# DFS - stack
				stack = [(i, j)]
				tmp = 0
				while stack:
					row, col = stack.pop()
					if matrix[row][col] == '.' or visited[row][col]: continue
					visited[row][col] = 1
					tmp += 1
					
					for k in range(4):
						nextY, nextX = row + dy[k], col + dx[k]
						
						if 0 <= nextY < n and 0 <= nextX < m and matrix[nextY][nextX] != '.' and not visited[nextY][nextX]:
							stack.append((nextY, nextX))
				
				# BFS
				# queue = deque([(i, j)])
				# tmp = 0
				# while queue:
				# 	row, col = queue.popleft()
				# 	if matrix[row][col] == '.' or visited[row][col]: continue
				# 	visited[row][col] = 1
				# 	tmp += 1
					
				# 	for k in range(4):
				# 		nextY, nextX = row + dy[k], col + dx[k]
				# 		if 0 <= nextY < n and 0 <= nextX < m:
				# 			if matrix[nextY][nextX] != '.' and not visited[nextY][nextX]:
				# 				queue.append((nextY, nextX))
				answer[0] += 1
				answer[1] = max(answer[1], tmp)
				
	print(f'{answer[0]}\n{answer[1]}')


solution()