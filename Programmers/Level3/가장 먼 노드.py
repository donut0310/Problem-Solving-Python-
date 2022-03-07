from collections import defaultdict,deque

def make_adjlist(n,edge):
    graph = defaultdict(list)
    for vertexes in edge:
        graph[vertexes[0]].append(vertexes[1])
        graph[vertexes[1]].append(vertexes[0])
    return graph

def solution(n, edge):
    answer = []
    queue,dist = deque([1]), [0]*(n+1)
    visited = [0]*(n+1)
    graph = make_adjlist(n,edge)
    dist[1]=1
    while len(queue):
        v=queue.popleft()
        if not visited[v]:
            visited[v]=1
            for i in graph[v]:
                queue.append(i)
                if not dist[i]:
                    dist[i]=dist[v]+1
    return dist.count(max(dist[2:]))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

# dist에 거리정보를 담는다
# 시작정점 (1) 에 대해 거리정보 갱신을 없애기 위해 dist[1]=1로 초기화한다.
# 이후 bfs를 통해 시작정점으로부터 각 정점까지의 최소거리들을 구한다.
# dist에 담긴 거리 정보중 최대값을 가진 노드들만 개수를 세서 반환한다.

