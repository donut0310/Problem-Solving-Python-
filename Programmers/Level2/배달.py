from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    dist = {}
    for i in range(1,N+1):
        dist[i]=500000
    dist[1]=0
    q=[(1,0)] #정점, 가중치, 방문

    for u,v,w in road:
        graph[u].append((v,w))
        graph[v].append((u,w))

    while q:
        node, d = heapq.heappop(q)
        if d>dist[node]:continue
        dist[node]=d
        for v,w in graph[node]:
            weight = d+w
            heapq.heappush(q,(v,weight))
    for i in dist:
        if dist[i]<=K:
            answer+=1
    return answer

# print(solution(5, [[1, 2, 4], [1, 3, 1], [3, 4, 1], [4, 2, 1], [2, 5, 1], ],4))
# print(solution(6,[[1,2,1],[1,3,2],[3,5,3],[2,3,2],[3,4,3],[3,5,2],[5,6,1]],4))
'''
풀이
"다익스트라 알고리즘 적용"
1. 각 정점까지의 최소거리를 저장할 dist dictionary 선언 및 초기화
2. 인접리스트 구현
3. 우선순위 큐 q 를 선언 후 (시작마을 번호, 거리) 삽입
4. 우선순위 큐에서 마을 정보를 꺼낸 후 dist에 저장된 최소 거리와 비교
4-1. 최소거리보다 크다면 skip
4-2. 최소거리보다 작다면 dist를 최신화
5. 4에서 꺼낸 마을에 인접한 마을들을 인접리스트에서 가져온 후 각각의 거리를 계산해 우선순위 큐에 삽입
6. 4,5 과정 반복 
'''