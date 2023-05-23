from collections import deque
import sys, math
input = sys.stdin.readline

def bfs(arr):
    visited = [[0] * n for _ in range(m)]
    candidates = deque([])

    for r, c in arr:
        if visited[r][c]: continue
        queue = deque([(r, c)])

        while queue:
            row, col = queue.popleft()

            if visited[row][col]: continue
            visited[row][col] = 1
            flag = 0

            for k in range(4):
                nextY, nextX = row + dy[k], col + dx[k]
                if 0 <= nextY < m and 0 <= nextX < n and matrix[nextY][nextX] != 'W' and not visited[nextY][nextX]:
                    flag = 1
                    queue.append((nextY, nextX))
            if not flag:
                candidates.append((row, col))
    
    return candidates

    

def solution():
    answer = set()
    arr = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'L': arr.append((i, j))


    for r, c in bfs(arr):
        distance = [[math.inf for _ in range(n)] for _ in range(m)]
        queue = deque([(r, c, 0)])

        while queue:
            row, col, d = queue.popleft()

            if distance[row][col] < d + 1: continue
            distance[row][col] = d

            answer.add(d)

            for i in range(4):
                nextY, nextX = row + dy[i], col + dx[i]    
                if 0 <= nextY < m and 0 <= nextX < n and matrix[nextY][nextX] != 'W' and distance[nextY][nextX] >= d + 1:
                    queue.append((nextY, nextX, d + 1))

    return max(answer)
        
            

m, n = map(int, input().rstrip().split(' '))
matrix = [list(input().rstrip()) for _ in range(m)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

print(solution())
