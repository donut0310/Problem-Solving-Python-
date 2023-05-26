from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while queue:
        row, col = queue.popleft()
    
        if matrix[d[0]][d[1]] == 'S': return # 비버 소굴에 고슴도치가 들어오면 종료

        for i in range(4):
            nextY, nextX = row + dy[i], col + dx[i]

            if 0 <= nextY < m and 0 <= nextX < n:
                if matrix[row][col] == 'S' and (matrix[nextY][nextX] == '.' or matrix[nextY][nextX] == 'D'):
                    time_info[nextY][nextX] = time_info[row][col] + 1
                    matrix[nextY][nextX] = 'S'
                    queue.append((nextY, nextX))
                elif matrix[row][col] == '*' and (matrix[nextY][nextX] == '.' or matrix[nextY][nextX] == 'S'):
                    matrix[nextY][nextX] = '*'
                    queue.append((nextY, nextX))


def solution():
    bfs()
    return time_info[d[0]][d[1]] if time_info[d[0]][d[1]] else "KAKTUS"


m, n = map(int, input().rstrip().split(' '))
matrix = [list(input().rstrip()) for _ in range(m)]
time_info = [[0 for _ in range(n)] for _ in range(m)]
queue, d = deque([]), None
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

# 고슴도치 위치 먼저 큐에 넣고, 물의 위치 큐에 넣기 => 고슴도치의 진행 과정에 물의 진행 과정을 덮어쓸 수 있음
for i in range(m):
   for j in range(n):
        if matrix[i][j] == 'S': queue.append((i, j))
        elif matrix[i][j] == 'D': d = (i, j)
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '*': queue.append((i, j))

print(solution())


'''
빈곳 => .
물 => *
돌 => X
비버 소굴 => D
고슴도치 => S

고슴도치는 인접한 네 칸으로 매분마다 이동(물, 돌로 이동 X)
    + 다음 시간에 물이 찰 예정인 칸으로 이동 역시 불가능
물은 인접한 비어있는 칸으로 매분마다 확장(돌, 비버 소굴로 이동 X)
'''