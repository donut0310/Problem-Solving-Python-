import sys
from collections import defaultdict,deque

N, M, V = map(int, sys.stdin.readline().strip().split())
adj = defaultdict(list)
for _ in range(M):
    v1,v2 = map(int,sys.stdin.readline().strip().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

def dfs(adj):
    for i in adj:
        adj[i].sort(reverse=True)
    visited = [0 for _ in range(N+1)]
    stack,answer=[V],[]
    while stack:
        tmp = stack.pop()
        if not visited[tmp]:
            visited[tmp]=1
            answer.append(tmp)
            stack.extend(adj[tmp])
    return answer

def bfs(adj):
    for i in adj:
        adj[i].sort() 
    queue,answer = deque([V]),[]
    visited = [0 for _ in range(N+1)]
    while queue:
        tmp = queue.popleft()
        if not visited[tmp]:
            visited[tmp]=1
            answer.append(tmp)
            for node in adj[tmp]:
                if not visited[node]:
                    queue.append(node)
    return answer

def solution(): # 정점의 개수, 간선의 개수, 시작 정점
    print(' '.join(map(str,dfs(adj))))
    print(' '.join(map(str,bfs(adj))))

solution()
