from collections import defaultdict

def solution(n, computers):
    answer = 0
    adj = defaultdict(list)
    for i in range(n): # 인접 리스트 구성
        for j in range(len(computers[i])):
            if not i==j and computers[i][j]==1: adj[i].append(j)
    
    visited = [0]*n
    for i in range(n): # 모든 정점에서 연결 정점 조사
        if not visited[i]: # 방문한적 없는 노드들만 진행
            visited[i]=1
            stack = adj[i] # 방문노드의 인접 노드들을 스택에 담는다
            while stack:
                tmp=stack.pop()
                if not visited[tmp]: # 방문한적 없는 노드들만 자신의 인접노드들을 스택에 담는다
                    stack.extend(adj[tmp])
                    visited[tmp]=1
            answer+=1
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# 스택을 이용한 DFS풀이로 접근
# 모든 정점에서 연결된 정점에 대하여 조사한다. -> 연결이 되어있지 않은 정점들도 있기 때문
# 대신 방문한 적이 있는 정점에 대해선 건너뛴다
# 시작 정점을 방문노드에 기록하고 스택에 시작 정점의 인접노드들을 추가한다.
# 스택에서 pop한 노드가 방문한 적이 없는 노드라면 역시 해당 노드의 인접노드들을 스택에 넣어준다.
# 스택이 빈 경우 노드간의 연결이 확인되었기에 answer값을 1 올려준다.