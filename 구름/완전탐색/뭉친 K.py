from collections import deque
import sys
input = sys.stdin.readline

def solution():
	answer = []
	
	n = int(input())
	x, y = map(int, input().split(' '))
	matrix = []
	
	for i in range(n):
		matrix.append(input().rstrip().split(' '))
	
	target = matrix[x-1][y-1]

	visited = [[0] * n for _ in range(n)]
	dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

	for i in range(n):
		for j in range(n):
			if visited[i][j] or matrix[i][j] != target: continue
			queue = deque([(i, j)])
			cnt = 0
			
			while queue:
				row, col = queue.popleft()
				if visited[row][col] or matrix[row][col] != target: continue
				visited[row][col] = 1
				cnt += 1
				
				for k in range(4):
					nextY, nextX = row + dy[k], col + dx[k]
					
					if 0 <= nextY < n and 0 <= nextX < n:
						if visited[nextY][nextX] or matrix[nextY][nextX] != target: continue
						queue.append((nextY, nextX))
			
			answer.append(cnt)
	
	return max(answer)
	
print(solution())