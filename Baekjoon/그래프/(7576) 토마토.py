import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split(' '))))

def solution():
    queue = deque([])
    tomato = n * m
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                queue.append((i, j, 0))
            elif matrix[i][j] == -1:
                tomato -= 1


    if len(queue) == tomato: 
        print('0')
        return
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * n for _ in range(m)]
    cost = 0

    while queue:
        row, col, d = queue.popleft()
        if visited[row][col]: continue
        visited[row][col] = 1
        tomato -= 1
        cost = max(cost, d)

        for i in range(4):
            next_y, next_x = row + dy[i], col + dx[i]
            if 0 <= next_y < m and 0 <= next_x < n and matrix[next_y][next_x] == 0 and not visited[next_y][next_x]:
                queue.append((next_y, next_x, d+1))

    if tomato > 0: print('-1')
    else: print(cost)

solution()