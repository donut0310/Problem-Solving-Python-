def make_adjmatrix(n,results):
    adj_matrix = [[0]*(n+1) for _ in range(n+1)]

    for i in results:
        adj_matrix[i[0]][i[1]]=1
        adj_matrix[i[1]][i[0]]=-1
    return adj_matrix

def solution(n, results):
    answer=0
    adj_matrix = make_adjmatrix(n,results)  

    # 플로이드 워셜
    for k in range(1,len(adj_matrix)): # 중간 노드
        for i in range(1,len(adj_matrix)):
            for j in range(1,len(adj_matrix)):
                if adj_matrix[i][j]==-1 or adj_matrix[j][i]==-1: continue
                if adj_matrix[i][k]==1 and adj_matrix[k][j]==1:
                    adj_matrix[i][j]=1
                    adj_matrix[j][i]=-1
    for i in adj_matrix:
        if i.count(0)==2:
            answer+=1                
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# results에 담긴 승패 정보를 adj_matrix에 기록한다.
# 이때 [a,b] => a 승 b 패 => adj_matrix[a][b]=승, adj_matrix[b][a]=패로 기록한다.
# 플로이드 워셜 알고리즘으로 각 노드들을 중간노드로(k) 시작노드(i), 도착노드(j)로 인덱스를 정한 후 노드들간의 연계를 기록한다.
# 이때 시작노드에서 중간노드로 가는 길이 양의 간선(승리)인 경우만 도착노드로의 연계 이어갈 수 있기 때문에 
# 시작노드에서 중간노드로 가는 길이 음의 간선(패배)인 경우는 무시한다.
# 모든 승패 정보가 업데이트 된 후 인접 행렬의 각 행에서 0인 정보(승패를 알 수 없는 정보)가 n-1인 경우만 
# 정확하게 순위를 매길 수 있는 경우이므로 이때 answer값을 더해준다.
# 위코드에선 0행 0열은 사용하지 않기 때문에 인접 행렬의 각 행에서 0의 개수가 n-2개 가 된 경우 정확하게 순위를 매길 수 있는 경우가 된다.