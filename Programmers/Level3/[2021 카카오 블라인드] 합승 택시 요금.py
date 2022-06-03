import math

''' 플로이드 워셜 이용 '''
def solution(n, s, a, b, fares): # n: 정점, s: 출발점, a: A의 도착지점, b: B의 도착지점
    answer = math.inf

    # 인접 행렬
    matrix = [[math.inf]*(n+1) for _ in range(n+1)]
    
    # 인접 행렬 초기화
    for start,end,weight in fares:
        matrix[start][end]=weight
        matrix[end][start]=weight

    # 플로이드 워셜
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
    
    # 합승하지 않는 경우
    answer = matrix[s][a]+matrix[s][b]
    
    # 합승하는 경우
    for i in range(1,n+1):
        if i==s: continue
        elif i==a:
            answer = min(answer,matrix[s][i]+matrix[i][b])
        elif i==b:
            answer = min(answer,matrix[s][i]+matrix[i][a])
        else:
            answer = min(answer,matrix[s][i]+matrix[i][a]+matrix[i][b])
    return answer


# print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) # 82
# print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])) # 14
# print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])) # 18

'''
<풀이>
문제 설명: A와 B가 각자의 도착지로 도달하기까지 최소 택시요금을 기준으로한 최단거리를 구하라
            이때, A와 B는 필요시 합승이 가능하다 -> 동시에 같은 루트를 갈 수 있다.

<알고리즘>
출발점에서 각 노드까지의 최단거리를 구한다 -> 플로이드 워셜(모든 정점끼리의 최단거리) 또는 다익스트라(특정 정점에서 모든 정점까지의 최단거리)

- 플로이드 워셜 이용
1. 인접 행렬 선언 및 초기화(math.inf)
2. 플로이드 워셜 알고리즘 사용
3. 합승한 경우와 합승하지 않은 경우로 나눈다.
3-1. 합승하지 않은 경우 출발점에서 A의 도착지, B의 도착지까지의 최소요금을 따로 계산
3-2. 합승한 경우에는 어디까지 합승을 같이 했는지를 분기해야한다.
    이때, A가 먼저 내린 경우와 B가 먼저 내린 경우, 특정 지점에서 둘 다 내려 각각 따로 택시를 다시 탄 경우 3가지로 분기한다.
4. 위 조건을 만족할 때의 answer값을 구해 반환한다.

'''