from itertools import combinations
import sys
input = sys.stdin.readline

def solution():
    answer = 2501
    house, chicken = [], []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1: house.append((i, j))
            elif matrix[i][j] == 2: chicken.append((i, j))

    arr = list(combinations(chicken, m))

    for i in range(len(arr)):
        total = 0

        for r1, c1 in house:
            d = 51

            for r2, c2 in arr[i]:
                d = min(d, abs(r1-r2) + abs(c1-c2))
            total += d
        answer = min(answer, total)

    return answer    
            
    

n, m = map(int, input().split(' '))
matrix = [list(map(int, input().rstrip().split(' '))) for i in range(n)]

print(solution())
