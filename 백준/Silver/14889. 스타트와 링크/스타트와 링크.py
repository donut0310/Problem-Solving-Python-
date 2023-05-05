from collections import deque
import sys, math
input = sys.stdin.readline

def dfs(cnt, idx):
    global answer
    
    if n // 2 == cnt:
        t1, t2 = 0, 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    t1 += matrix[i][j]
                elif not visited[i] and not visited[j]:
                    t2 += matrix[i][j]
                
        answer = min(abs(t1 - t2), answer)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, i+1)
            visited[i] = 0

n = int(input())

answer = math.inf
matrix = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
visited = [0 for _ in range(n)]

dfs(0, 0)
print(answer)
    
