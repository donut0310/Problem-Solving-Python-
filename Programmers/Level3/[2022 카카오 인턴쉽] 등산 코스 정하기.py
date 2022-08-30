from collections import defaultdict
import heapq
import math

def solution(n, paths, gates, summits):
    answer = []
    graph = defaultdict(list)

    for start, end, d in paths:
        graph[start].append((end,d))
        graph[end].append((start,d))
    
    summits = set(summits)
    inten_info = [math.inf] * (n+1)
    queue = []

    for gate in gates:
        heapq.heappush(queue, (gate,0))
    
    while queue:
        node, d = heapq.heappop(queue)
        if node in summits or inten_info[node] < d: continue

        for next_node, next_d in graph[node]:
            inten = max(d, next_d)
            if inten < inten_info[next_node]:
                inten_info[next_node] = inten
                heapq.heappush(queue,(next_node, inten))

    
    for summit in summits:
        answer.append((summit, inten_info[summit]))
    
    answer.sort(key=lambda x: (x[1],x[0]))
    return answer[0]

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])) # [5, 3]


'''
<풀이>

다익스트라 알고리즘 사용
1. 출발점들을 큐에 삽입한다.
2. 큐에서 하나의 노드 정보를 추출한다.
3. 현재 노드가 '정상'에 해당하는 노드이거나, intentsity 에 기록된 거리보다 크다면 스킵
4. 3에 해당하지 않을 경우, 현재 노드의 인접노드들을 탐색하며, intensity값을 조정한 후, 조건에 맞게 큐에 삽입한다.
4-1. intensity 값은 진행 중인 경로에 현재보다 큰 값이 있다면, 큰 값을 우선적으로 따라야 하기에 현재 노드까지의 intensity 값과
    다음 노드를 진행했을 때의 intensity값을 비교해 큰 값을 선택해야한다.
'''