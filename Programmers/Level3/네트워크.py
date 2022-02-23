from collections import defaultdict
from collections import deque
import copy

visited = []
graph=defaultdict(deque)

def dfs(v):
    global visited
    global graph
    visited[v]=True
    connected_nodes = deque(graph[v])

    for i in copy.deepcopy(connected_nodes):
        connected_nodes.popleft()
        graph[v]=connected_nodes
        if not visited[i]:
            dfs(i)
    return 1

def make_adjlist(n,computers):
    global graph
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1: graph[i].append(j)

def solution(n, computers):
    answer = 0
    global visited
    global graph
    
    [visited.append(False) for i in range(n)]
    make_adjlist(n,computers)
    for i in range(n):
        if len(graph[i]):
            answer+=dfs(i)
    visited=[]
    graph=defaultdict(deque)
    return answer

# print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# print(solution(5,[[1,1,0,0,1],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[1,0,0,0,1]]))

# 인접리스트를 이용한 재귀 풀이 DFS 방식 적용
# 모든 정점에서 출발해 중복되지않은 사이클마다 네트워크가 +1 되기 때문에 메인함수에서 모든 정점마다 DFS를 호출한다.
# 방문 노드를 찍을때 각 정점에 연결된 정점에 대해서 popleft로 리스트에서 삭제한다.
# 이렇게 되면 main함수에서 각 정점마다 DFS를 호출할 때 인접리스트가 [] 인 경우엔 DFS를 호출하지 않게 된다.
# DFS를 통해 사이클이 구해지면 answer+=1을 통해 네트워크의 수를 카운팅한다.