from collections import deque, defaultdict

def solution():
	r, c, k = map(int, input().split(' '))
	answer = 0
	
	matrix = [[0] * c for _ in range(r)]
	for i in range(r):
		tmp = input()
		for j in range(len(tmp)):
			matrix[i][j] = int(tmp[j])
	
	queue = deque([(0, 0, k, 0)]) # row, col, k, cost
	dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
	visited = defaultdict(set)
	visited[k].add((0, 0)) # 시작점 초기화
	
	while queue: 
		row, col, k, cost = queue.popleft()
		
		if row == r-1 and col == c-1: 
			return cost

		for i in range(4):
			nextY, nextX = row + dy[i], col + dx[i]

			if 0 <= nextY < r and 0 <= nextX < c and (nextY, nextX) not in visited[k]:
				if matrix[nextY][nextX]:
					if k >= 10:
						nextY += dy[i]
						nextX += dx[i]

						if 0 <= nextY < r and 0 <= nextX < c and k >= 10 and not matrix[nextY][nextX]:
							queue.append((nextY, nextX, k-10, cost+1))
							visited[k-10].add((nextY, nextX))

				else: 
					queue.append((nextY, nextX, k, cost+1))
					visited[k].add((nextY, nextX))

	return -1
	
print(solution())
