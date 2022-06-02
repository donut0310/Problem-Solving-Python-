from collections import deque

def solution(board):
    queue = deque([(len(board)-1,len(board)-1,0,[len(board)-1,len(board)-1])]) # ((x,y,fee,(prev x, prev y)) => 현재 x축, 현재 y축, 현재 지점까지의 요금, 이전 지점의 x,y축
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    # 최단거리(요금 기준) 테이블
    dist = {}
    for i in range(len(board)):
        for j in range(len(board)):
            dist[(i,j)] = 0
            
    # BFS
    while queue:
        x,y,fee,prev = queue.popleft()
        for i in range(4):
            nextX = x+dx[i]
            nextY = y+dy[i]
            if (nextX>=0 and nextX<len(board)) and (nextY>=0 and nextY<len(board)) and board[nextY][nextX]!=1: # board 범위 내, 벽이 아닌 경우
                if x==y==0: # 시작점인 경우 무조건 직진
                    queue.append((nextX,nextY,fee+100,(x,y)))
                    dist[(nextX,nextY)] = fee+100
                    continue
                if nextX==prev[0] and nextY==prev[1]:
                    continue
                # 요금 계산
                if prev[0]!=nextX and prev[1]!=nextY: # 코너 건설
                    if dist[(nextX,nextY)] and fee+600 > dist[(nextX,nextY)]: continue # 다음 행선지에 방문한 적 있다면, 현재 지점에서 추가한 요금이 다음 행선지에 저장된 요금보다 비싸다면 스킵
                    queue.append((nextX,nextY,fee+600,(x,y)))
                    dist[(nextX,nextY)] = fee+600
                else: # 직진 건설
                    if dist[(nextX,nextY)] and fee+100 > dist[(nextX,nextY)]: continue 
                    queue.append((nextX,nextY,fee+100,(x,y)))
                    dist[(nextX,nextY)] = fee+100
    return dist[(0,0)]

print(solution([[0,0,0],[0,0,0],[0,0,0]])) # 900
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])) # 3800
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])) # 2100
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])) # 3200

# 테케 25번
print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]])) # 4500

'''
풀이: BFS

출발지를 정한 후 BFS를 이용해 도착지점까지의 최단거리(요금 기준)을 구한다.
현재 위치에서 갈 수 있는 지점을 검사한 후 해당 지점의 좌표와, 해당지점까지의 요금, 이전 위치의 좌표를 큐에 저장한다.
코너 도로 건설 => 현재 위치 기준 두 위치 전에 좌표와 비교해 x,y값이 모두 다른 경우에 해당한다.
직진 도로 건설 => 코너 도로 건설 조건에 만족하지 않는 경우에 해당한다.

<데이터>
dist => 각 좌표까지의 최소요금
queue => BFS에 이용할 큐, 각 원소는 다음 위치의 좌표와 다음 위치까지의 요금, 현재 위치의 좌표를 가진다.

<알고리즘>
1. 각 지점에서 4방향을 검사한 후 갈 수 있는 곳으로만 움직인다.
2. 시작점인 경우 무조건 직진 도로를 건설한 후 큐에 직진도로를 건설할 다음 위치의 정보를 삽입한다. 
2-1. 이때, 코너 건설의 조건을 검사하기 위한 현재 위치의 이전 위치의 정보를 따로 저장한다 => (prevX, prevY)
3. 다음 위치의 좌표를 삽입할 때 만약 방문한 적 있는 곳이라면, dist 테이블과 비교해 요금이 더 싼 경우를 채택한다.

<고려사항>
시작점을 [0,0] 으로 지정하면 도착점으로 가는 모든 경우의 수를 찾다가 테케 25번의 과정을 만족시키지 못한다.
반대로 도착점[n,n]에서 출발해 시작점으로 가면, 최선의 길을 찾을 수 있다. 
'''