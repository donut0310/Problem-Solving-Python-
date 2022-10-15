from collections import deque, defaultdict

def solution(n, computers):
    answer = 0
    graph = defaultdict(set)
    
    # 그래프 연결 초기화
    for i, node_info in enumerate(computers):
        for j, info in enumerate(node_info):
            if i==j: continue
            if info:
                graph[i+1].add(j+1)
                graph[j+1].add(i+1)
                
    # BFS
    visited = [0] * n
    for i in range(1, n+1): # 모든 정점에서 시작하는 연결구조 확인해야함
        if visited[i-1]: continue # 시작정점이 방문한 적 있다면, 새로운 네트워크 형성 X
        queue = deque([i])
        
        while queue:
            node = queue.popleft()
            visited[node-1] = 1
            for next in graph[node]:
                if not visited[next-1]: queue.append(next) # 방문한적 없는 노드만 추가
        answer += 1
    
    return answer