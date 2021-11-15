from collections import deque

def solution(maps):
    answer=1 #시작은 무조건 거리 1
    n, m = len(maps), len(maps[0])
    maps [n-1][m-1] =- 1 #도착지에 도달 할 수 없음을 가정해 우선 -1로 초기화
    #상하좌우
    dx = [-1,1,0,0] 
    dy = [0,0,-1,1]
    q = deque()
    q.append((0,0,answer)) #우선순위 큐에 출발지 삽입

    visited = [[0]*m for _ in range(n)] #방문 여부

    while q:
        x,y,answer=q.popleft()
        for i in range(4): #4방향 조사
            nx,ny = x+dx[i],y+dy[i]
            if -1<nx<n and -1<ny<m: #맵 범위 내에 있는 경우
                if maps[nx][ny] and visited[nx][ny]==0: #벽이 아니고 방문한 적이 없는 경우
                    maps[nx][ny]=answer+1
                    visited[nx][ny]=1
                    q.append((nx,ny,answer+1))
    return maps[n-1][m-1]
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))