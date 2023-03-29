import sys
input = sys.stdin.readline

n, m = map(int, input().split())
def dfs(num, visited, cnt, stack):
    if visited[num-1]: return
    
    visited[num-1] = 1
    stack.append(num)
    cnt += 1
    if cnt == m: 
        [print(i, end=' ') for i in stack]
        print()
        stack.pop()
        visited[num-1] = 0
        return
    
    for i in range(1, n+1):
        dfs(i, visited, cnt, stack)
    stack.pop()
    visited[num-1] = 0
    return

def solution():
    for i in range(1, n+1):
        visited = [0] * n
        cnt = 0
        stack = []
        dfs(i, visited, cnt, stack)        
        
solution()