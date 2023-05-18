import sys
input = sys.stdin.readline

def dfs(color, r, c, toRow, toCol, cnt):
    nextRow, nextCol = r + toRow, c + toCol

    if 0 <= nextRow < n and 0 <= nextCol < n:
        if color == matrix[nextRow][nextCol]:
            cnt = dfs(color, nextRow, nextCol, toRow, toCol, cnt+1)    

    return cnt


def solution():
    answer = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nextRow, nextCol = i + dy[k], j + dx[k]

                if 0 <= nextRow < n and 0 <= nextCol < n:
                    matrix[i][j], matrix[nextRow][nextCol] = matrix[nextRow][nextCol], matrix[i][j]
                    # 행 탐색
                    rowCnt = dfs(matrix[i][j], i, j, 1, 0, 1) + dfs(matrix[i][j], i, j, -1, 0, 1) - 1 # i,j 위치값 중복되기에 -1
                    # 열 탐색
                    colCnt = dfs(matrix[i][j], i, j, 0, 1, 1) + dfs(matrix[i][j], i, j, 0, -1, 1) - 1
                    answer = max(answer, rowCnt, colCnt)
                    matrix[i][j], matrix[nextRow][nextCol] = matrix[nextRow][nextCol], matrix[i][j]
    return answer

n = int(input())
matrix = [list(input().rstrip()) for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

print(solution())

