from collections import defaultdict, deque

def bfs(towers, node_info, n):
    queue = deque([towers[0]])
    opposite = towers[1]
    visted = [0 for _ in range(n+1)]
    cnt = 0
    while queue:
        node = queue.popleft()
        if not visted[node]:
            visted[node] = 1
            cnt += 1
            for adj_node in node_info[node]:
                if not visted[adj_node] and adj_node != opposite: # 방문한 적이 없고, 끊어진 노드가 아닐 때
                    queue.append(adj_node)
    return cnt

def solution(n, wires):
    answer = 100
    node_info = defaultdict(list)

    for wire_a, wire_b in wires:
        node_info[wire_a].append(wire_b)
        node_info[wire_b].append(wire_a)
    
    for node in node_info:
        towers = [node, 0]
        for adj_node in node_info[node]:
            towers[1] = adj_node
            answer = min(answer, abs(bfs(towers, node_info, n) - bfs(towers[::-1], node_info, n)))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3
print(solution(4, [[1,2],[2,3],[3,4]])) # 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) # 1

'''
<풀이>
선택된 노드와, 선택된 노드의 인접노드들을 각각 타워1, 타워2로 나눈 후, 
각각의 노드를 시작점으로 하는 BFS 탐색을 이용한다.
위 과정을 전체 노드 수(n) 만큼 반복하여 모든 노드에 대해서 탐색한다.

위 문제는 노드의 정보가 트리로 보장되기 때문에 사이클이 존재할 수 없다. 
따라서 두 개의 노드를 선택하여 각각의 노드를 시작점으로하는 BFS 탐색을 이용할 때,
상대 노드를 방문하면 큐에 추가하지 않는 분기문을 사용한다면 각각의 경우에 개별적인 BFS 탐색이 가능하다고 생각했고,
문제를 해결할 수 있었다.
'''