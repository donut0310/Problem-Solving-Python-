from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr):
    result = 0
    visited = [[0] * n for i in range(n)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    for r, c in arr:
        if visited[r][c]: continue
        
        queue = deque([(r, c)])

        while queue:
            row, col = queue.popleft()

            if visited[row][col]: continue
            visited[row][col] = 1

            for i in range(4):
                nextRow, nextCol = row + dy[i], col + dx[i]
                if 0 <= nextRow < n and 0 <= nextCol < n and matrix[nextRow][nextCol] > 0 and not visited[nextRow][nextCol]:
                    queue.append((nextRow, nextCol))
        
        result += 1
    return result


def solution():
    answer = 1
    max_height = 0
    for i in range(n):
        for j in range(n):
            max_height = max(max_height, matrix[i][j])

    for i in range(max_height):
        arr = []
        for j in range(n):
            for k in range(n):
                matrix[j][k] -= 1 

                if matrix[j][k] > 0: 
                    arr.append((j, k))

        answer = max(answer, bfs(arr))
    return answer
    
n = int(input())
matrix = [list(map(int, input().rstrip().split(' '))) for i in range(n)]

print(solution())