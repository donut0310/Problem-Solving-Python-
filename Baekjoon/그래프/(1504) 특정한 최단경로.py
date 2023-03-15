from collections import defaultdict
import sys, heapq, math

input = sys.stdin.readline

V, E = map(int, input().split(' '))

graph = defaultdict(list)

for i in range(E):
    u, v, e = map(int, input().split(' '))
    graph[u].append((v, e))
    graph[v].append((u, e))

v1, v2 = map(int, input().split(' '))

def bfs(start, end):
    table = [math.inf] * (V+1)
    queue = [(0, start)]
    table[start] = 0

    while queue:
        d, node = heapq.heappop(queue)
        if d > table[node]: continue

        for next_node, w in graph[node]:
            cost = w + d
            if cost < table[next_node]:
                table[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return table[end]

def solution():
    answer = min(bfs(1, v1) + bfs(v1, v2) + bfs(v2, V), bfs(1, v2) + bfs(v2, v1) + bfs(v1, V))

    if answer < math.inf: print(answer)
    else: print(-1)

solution()

'''
<풀이>
두 정점 v1, v2를 지나는 최단 거리를 구해야한다.
다익스트라 알고리즘을 이용해 시작점 1에서 시작한다.
1 -> v1 -> v2 -> N으로 가는 최단 거리와 1 -> v2 -> v1 -> N으로 가는 최단 거리 중
작은 값이 정답이 된다.
'''