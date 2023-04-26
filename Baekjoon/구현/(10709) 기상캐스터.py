import sys

input = sys.stdin.readline
m, n = map(int, input().split(' '))
city = [list(input().rstrip()) for _ in range(m)]

def solution():
    matrix = [[-1 for _ in range(n)] for _ in range(m)]
    
    # 구름 위치 0
    for i in range(m):
        for j in range(n):
            if city[i][j] == 'c': matrix[i][j] = 0

    # 각 행마다 누적합
    for row in matrix:
        for i in range(1, len(row)):
            if row[i] == 0 or row[i-1] == -1: continue
            row[i] += row[i-1] + 2
        [print(i, end=' ') for i in row]
        print()
solution()