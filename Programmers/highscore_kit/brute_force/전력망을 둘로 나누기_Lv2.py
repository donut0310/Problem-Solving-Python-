from collections import defaultdict, deque
import math

def bfs(graph, v1, v2):
    queue = deque([v1])
    visited = [0] * (len(graph) + 1)
    cnt = 0

    while queue:
        node = queue.popleft()
        if visited[node] or node == v2: continue
        cnt += 1
        visited[node] = 1

        for next in graph[node]:
            if not visited[next]:
                queue.append(next)

    return cnt

def solution(n, wires):
    answer = math.inf
    graph = defaultdict(list)

    for v, w in wires: # 그래프 생성
        graph[v].append(w)
        graph[w].append(v)
    
    for v, w in wires: # 송전탑 나눈 후 각각 bfs
        differ = abs(bfs(graph, v, w) - bfs(graph, w, v))
        answer = min(answer, differ)

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3