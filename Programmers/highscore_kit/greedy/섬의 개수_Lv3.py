def union(u, v, parent):
    r1 = find(u, parent)
    r2 = find(v, parent)
    if r1 == r2: return False
    if r1 < r2: parent[r2] = r1
    else: parent[r1] = r2
    return True

def find(node, parent):
    # 부모노드가 자기자신인 경우 -> 다른 집합에 속하지 않는다.
    if parent[node] == node: return node
    else: return find(parent[node], parent) # 다른 집합에 속하는 경우 부모 노드를 찾아간다.

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)] # 각 정점의 부모노드 배열, 각 정점의 부모노드는 자기 자신으로 초기화
    
    costs.sort(key=lambda x:x[2]) # 간선의 가중치를 기준으로 오름차순 정렬

    cnt = 0 # 연결된 간선의 개수
    
    for u, v, w in costs:
        if union(u, v, parent): # 부모노드가 다른 경우 병합 
            answer += w
            cnt += 1
        if cnt == n - 1: break # 연결된 간선의 개수가 정점의 총 개수 - 1인 경우 모든 정점간의 연결이 완료되었기 때문에 종료
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4
