import sys, math
input = sys.stdin.readline

def solution():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j: continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(n):
        for j in range(n):
            if graph[i][j] < math.inf: print(graph[i][j], end=' ')
            else: print(0, end=' ')
        print()

n = int(input())
m = int(input())
graph = [[math.inf] * n for _ in range(n)]

for i in range(m):
    start, end, cost = map(int, input().rstrip().split(' '))
    graph[start-1][end-1] = min(graph[start-1][end-1], cost)

solution()
