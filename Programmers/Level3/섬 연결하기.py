from collections import defaultdict

# 노드의 루트노드 찾기 
def find(node,cycle):
    if cycle[node] == node: return node
    else: return find(cycle[node],cycle)

# 간선의 양쪽 노드들의 집합 구성
def union(a,b,cycle):
    a = find(a,cycle)
    b = find(b,cycle)
    if a==b: return False
    if a<b: cycle[b]=a
    else: cycle[a]=b
    return True

def solution(n, costs):
    answer=0
    cycle = defaultdict(int)
    # 사이클 테이블 초기화
    for i in range(n): cycle[i]=i

    # 간선 기준 오름차순 정렬
    costs.sort(key = lambda x:x[2])
    edges = 0

    #크루스칼 알고리즘 적용 => MST 
    for cost in costs:
        if union(cost[0],cost[1],cycle): # 각 노드의 부모노드가 다른 경우에만 간선 연결
            answer+=cost[2]
            edges+=1
        if edges==n-1:break
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) #4
print(solution(5,[[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]])) #15
print(solution(5,[[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])) # 8
print(solution(6,[[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])) # 11
print(solution(5,[[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]])) #8
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])) #104
print(solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]])) #8
print(solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]])) #6
print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]])) #9
print(solution(5,[[0,1,1],[3,4,1],[1,2,2],[2,3,4]])) #8
print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]])) #9
print(solution(5,[[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]])) #8
print(solution(5,[[0,1,1],[0,2,2],[1,2,5],[2,3,8],[3,4,1]])) #12

'''
풀이
그리디 알고리즘 유형인 크루스칼 알고리즘(MST)을 사용
1. 각 노드와 간선의 정보가 담긴 costs 배열을 간선 무게를 key로 오름차순 정렬
2. 첫번째 노드집합부터 union-find 알고리즘을 통해 부모노드의 동일 여부를 파악한다.
3. 부모노드가 다른 경우에만 각 노드를 간선으로 연결하고 그때의 간선 무게를 answer에 더해준다
4. 모든 간선이 연결되었을 때 간선의 개수는 노드의 개수 -1개 이므로 해당 조건을 만족하면 반복문을 탈출한다.

막힌부분
각 노드집합을 union 함수를 호출하면서 똑같이 최상단 부모노드를 찾았어야 했는데, 
union 함수를 호출하지 않고 cycle(사이클 테이블)에서 바로 루트노드를 찾아 버리는 바람에 테케를 통과할 수 없었다.
'''