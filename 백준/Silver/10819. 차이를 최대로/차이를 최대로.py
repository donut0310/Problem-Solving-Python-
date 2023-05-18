import sys
input = sys.stdin.readline

def dfs(start, arr, cnt):
    visited[start] = 1

    arr.append(queue[start])

    for idx in range(n):
        if visited[idx]: continue
        dfs(idx, arr, cnt+1)
    
    if cnt == n: combs.append(arr[::])

    arr.pop()
    visited[start] = 0
    return


def calculate(arr):
    result = 0
    for i in range(n-1):
        result += abs(arr[i] - arr[i+1])

    return result


answer = 0
n = int(input())
queue = list(map(int, input().rstrip().split()))
visited = [0] * n
combs = []
    
for i in range(n):
    arr = []
    dfs(i, arr, 1)

for item in combs:
    answer = max(answer, calculate(item))
    
print(answer)

