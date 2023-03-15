from collections import defaultdict
import sys, heapq, math

input = sys.stdin.readline

V, E = map(int, input().split(' '))
start = int(input())
graph = defaultdict(list)
table = [math.inf] * (V + 1)

for i in range(E):
    u, v, e = map(int, input().split(' '))
    graph[u].append((v, e))

def solution():
    queue = [(0, start)]
    table[start] = 0
    
    while queue:
        d, node = heapq.heappop(queue)
        if table[node] < d: continue

        for next_node, w in graph[node]:
            cost = w + d
            if cost < table[next_node]:
                table[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    for i in range(1, V+1):
        if table[i] < math.inf: print(table[i])
        else: print('INF')

solution()

'''
<풀이>
전형적인 다익스트라 문제
주의: 시작 정점에 한해서 거리 테이블의 초기값을 0으로 만들어 두지 않으면 메모리 초과가 발생한다.. 왜..?
'''