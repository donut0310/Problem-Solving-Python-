from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(graph, queue, n, cnt):
	visited = [0] * (n+1)
	
	while queue:
		node = queue.popleft()
		
		if visited[node]: continue
		visited[node] = 1
		cnt += 1
		
		for next_node in graph[node]:
			if not visited[next_node]:
				queue.append(next_node)
	
	return cnt
			
	
def solution():
	n, m = map(int, input().split(' '))
	b_graph, s_graph = defaultdict(list), defaultdict(list)
	
	set_arr = set()
	for i in range(m):
		a, b = map(int, input().split(' '))
		set_arr.add((a, b))
	
	for a, b in set_arr:
		b_graph[b].append(a)
		s_graph[a].append(b)
	

	for i in range(1, n+1):
		cnt1, cnt2 = 0, 0
		
		queue1 = deque(b_graph[i]) if b_graph[i] else deque([])
		queue2 = deque(s_graph[i]) if s_graph[i] else deque([])
		
		print(f'{bfs(b_graph, queue1, n, cnt1)} {bfs(s_graph, queue2, n, cnt2)}')
		
solution()