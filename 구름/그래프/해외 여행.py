from collections import defaultdict
import sys, math, heapq
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split(' '))
	
	graph = defaultdict(list)
	dist = [math.inf] * (n+1)
	
	for i in range(m):
		u, v, w = map(int, input().split(' '))		
		graph[u].append((v, w))
	
	queue = [(1, 0)]

	while queue:
		node, d = heapq.heappop(queue)
		
		if d > dist[node]: continue
		dist[node] = d
		
		for next_node, w in graph[node]:
			cost = w + d
			if cost > dist[next_node]: continue
			heapq.heappush(queue, (next_node, cost))

	
	return dist[n] if dist[n] < math.inf else 'go home'

print(solution())