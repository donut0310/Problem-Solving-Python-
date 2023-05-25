from collections import deque
import sys
input = sys.stdin.readline

def solution():
    area_cnt = 0
    areas = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 or visited[i][j]: continue

            queue = deque([(i, j)])
            cnt = 0

            while queue:
                row, col = queue.popleft()
                if visited[row][col]: continue
                
                visited[row][col] = 1
                cnt += 1

                for l in range(4):
                    nextY, nextX = row + dy[l], col + dx[l]

                    if 0 <= nextY < n and 0 <= nextX < m and not visited[nextY][nextX] and not matrix[nextY][nextX]:
                        queue.append((nextY, nextX))

            area_cnt += 1
            areas.append(cnt)

    areas.sort()
    
    print(area_cnt)
    [print(i, end=' ') for i in areas]
    


m, n, k = map(int, input().rstrip().split(' '))
matrix = [[0] * (m) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().rstrip().split(' '))
    for j in range(x1, x2):
        for l in range(y1, y2):
            matrix[j][l] = 1

solution()