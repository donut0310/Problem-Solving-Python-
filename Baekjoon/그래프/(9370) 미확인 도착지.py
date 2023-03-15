from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

testcase = int(input())

def bfs(start, n, graph):
    table = [sys.maxsize] * (n + 1)
    table[start] = 0
    queue = [(0, start)] # 거리, 정점

    while queue:
        d, node = heapq.heappop(queue)
        if d > table[node]: continue

        for next_node, w in graph[node]:
            cost = w + d
            if cost < table[next_node]:
                table[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
    return table

def solution():
    for _ in range(testcase):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        graph = defaultdict(list)
        answer = []

        for _ in range(m):
            u, v, e = map(int, input().split())
            graph[u].append((v, e))
            graph[v].append((u, e))

        dist_start = bfs(s, n, graph)
        dist_g = bfs(g, n, graph)
        dist_h = bfs(h, n, graph)

        for _ in range(t):
            candidate = int(input())
            if dist_start[g] + dist_g[h] + dist_h[candidate] == dist_start[candidate] or dist_start[h] + dist_h[g] + dist_g[candidate] == dist_start[candidate]:
                answer.append(candidate)

        print(*sorted(answer))
            
solution()

'''
<풀이>
최대 정수값을 지정할 때 
math.inf 로 했더니 계속해서 오답처리가 되었다.
이 부분을 sys.maxsize로 하니 정답처리가 되었다.
math.inf -> inf (float 자료형) <class 'float'>
sys.maxsize -> 9223372036854775807 (int 자료형) <class 'int'>

자료형의 차이 때문에 발생하는 오류였던 것으로 생각된다.
'''