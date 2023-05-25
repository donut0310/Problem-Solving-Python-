from collections import deque
import sys
input = sys.stdin.readline

def bfs(flag):
    result = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue
            current_color = matrix[i][j]
            queue = deque([(i, j)])

            while queue:
                row, col = queue.popleft()
                
                if visited[row][col]: continue
                visited[row][col] = 1

                for k in range(4):
                    nextY, nextX = row + dy[k], col + dx[k]      

                    if 0 <= nextY < n and 0 <= nextX < n and not visited[nextY][nextX]:
                        if flag: # 적록색약 O
                            if (current_color == 'R' or current_color == 'G') and matrix[nextY][nextX] != "B":
                                queue.append((nextY, nextX))
                            elif current_color == 'B' == matrix[nextY][nextX]:
                                queue.append((nextY, nextX))
                        else: # 적록색약 X
                            if matrix[nextY][nextX] == current_color:
                                queue.append((nextY, nextX))

            result += 1

    return result


def solution():
    return f'{bfs(0)} {bfs(1)}'


n = int(input())
matrix = [list(input().rstrip()) for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

print(solution())