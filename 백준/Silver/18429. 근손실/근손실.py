import sys
input = sys.stdin.readline 

def dfs(start, weight, day, arr):
    weight += kits[start] - k    
    if weight < 500: return

    visited[start] = 1
    arr.append(start)

    if len(arr) == n:
        answer.append(arr)

    for i in range(n):
        if not visited[i]:
            dfs(i, weight, day + 1, arr)

    visited[start] = 0
    arr.pop()



n, k = map(int, input().rstrip().split(' '))
kits = list(map(int, input().rstrip().split(' ')))
visited = [0] * n
answer, weight = [], 500

for i in range(n):
    arr = [i]
    dfs(i, weight, 1, arr)

print(len(answer))

