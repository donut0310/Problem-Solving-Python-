import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())

def solution():
    matrix = []
    # 초기화
    for i in range(h):
        floor = []
        for j in range(n):
            floor.append(list(map(int, input().split())))
        matrix.append(floor)

    # 익은 토마토가 들어있는 위치들 추가
    queue = deque([])
    tomato = m*n*h # 익지 않은 토마토
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if matrix[i][j][k] == 1: 
                    queue.append((i, j, k, 0)) # 높이, 가로, 세로, 일 수
                elif matrix[i][j][k] == -1: tomato -= 1 # 토마토가 들어있지 않은 칸

    # 저장할 때 부터 토마토가 모두 익은 경우
    if len(queue) == tomato: return '0'

    # BFS
    dy, dx, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1] # 앞, 뒤, 좌, 우, 상, 하
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    days = 0

    while queue:
        height, row, col, d = queue.popleft()
        if visited[height][row][col]: continue
        visited[height][row][col] = 1
        tomato -= 1

        # 최초의 익은 토마토들을 기준으로 너비 탐색을 진행하기 때문에 각 칸의 토마토들이 익는데 시간은 모두 다르다.
        # 따라서 전체 일 수를 갱신하려면 각 토마토가 익는데까지 걸리는 최대 시간으로 갱신해야 한다.
        days = max(days, d)

        for i in range(6):
            next_h, next_y, next_x = height + dz[i], row + dy[i], col + dx[i]

            if 0 <= next_y < n and 0 <= next_x < m and 0 <= next_h < h and matrix[next_h][next_y][next_x] == 0 and not visited[next_h][next_y][next_x]:
                queue.append((next_h, next_y, next_x, d + 1))

    if tomato > 0: return '-1'
    return days

print(solution())
