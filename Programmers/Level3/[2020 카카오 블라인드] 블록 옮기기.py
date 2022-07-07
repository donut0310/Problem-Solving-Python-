from collections import deque
def dot_check(queue,a,b,d):
    if a[0]<=b[0] and a[1]<=b[1]: queue.append((a,b,d+1))
    else: queue.append((b,a,d+1))
    return queue

def solution(board):
    n = len(board)
    visited = [[(0,0,0)] * n for _ in range(n)] # 가로 방문여부 세로 방문 여부, 시간    
    queue = deque([((0,0),(0,1),0)]) # 원소 => ((좌표1),(좌표2), 시간)
    target = (n-1,n-1)

    # 상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    while(queue):
        a,b,d = queue.popleft() # 두 좌표의 정보 ((x1,y1),(x2,y2),시간)

        # 방문 처리 및 시간계산
        if b[0]-a[0]==0: # 수평인 경우
            if visited[a[0]][a[1]][0] and visited[b[0]][b[1]][0]: continue 
            visited[a[0]][a[1]] = (1,visited[a[0]][a[1]][1],d)
            visited[b[0]][b[1]] = (1,visited[b[0]][b[1]][1],d)
        elif b[1]-a[1]==0: # 수직인 경우
            if visited[a[0]][a[1]][1] and visited[b[0]][b[1]][1]: continue 
            visited[a[0]][a[1]] = (visited[a[0]][a[1]][0],1,d)
            visited[b[0]][b[1]] = (visited[b[0]][b[1]][0],1,d)

        if a == target or b == target: return d # 두 점 중 하나라도 (n,n)에 도달하면 종료

        # 회전
        if b[0]-a[0]==0: # 두 점이 수평인 경우
            left = [(-1,-1),(1,-1)] # 왼쪽 점 기준 상, 하
            for i in left:       
                row,col = b[0]+i[0], b[1]+i[1]
                if (0<=row<n and 0<=col<n) and board[row][col]!=1 and board[row][col+1]!=1:
                    if visited[a[0]][a[1]][1]==1 and visited[row][col][1]==1: continue
                    queue = dot_check(queue,a,(row,col),d)
            right = [(-1,1),(1,1)] # 오른쪽 점 기준 상, 하
            for i in right:
                row,col = a[0]+i[0], a[1]+i[1]
                if (0<=row<n and 0<=col<n) and board[row][col]!=1 and board[row][col-1]!=1:
                    if visited[b[0]][b[1]][1]==1 and visited[row][col][1]==1: continue
                    queue = dot_check(queue,b,(row,col),d)
        elif b[1]-a[1]==0: # 두 점이 수직인 경우
            up = [(-1,-1),(-1,1)] # 위쪽 점 기준 좌, 우
            for i in up:
                row,col = b[0]+i[0], b[1]+i[1]
                if (0<=row<n and 0<=col<n) and board[row][col]!=1 and board[row+1][col]!=1:
                    if visited[a[0]][a[1]][0]==1 and visited[row][col][0]==1: continue
                    queue = dot_check(queue,a,(row,col),d)
            down = [(1,-1),(1,1)] # 아래쪽 점 기준 좌, 우
            for i in down:
                row,col = a[0]+i[0], a[1]+i[1]
                if (0<=row<n and 0<=col<n) and board[row][col]!=1 and board[row-1][col]!=1:
                    if visited[b[0]][b[1]][0]==1 and visited[row][col][0]==1: continue
                    queue = dot_check(queue,b,(row,col),d)
        # 상하좌우 칸 이동
        for i in range(4):
            dy_a, dx_a = a[0]+dy[i], a[1]+dx[i]
            dy_b, dx_b = b[0]+dy[i], b[1]+dx[i]
            if (0 <= dy_a < n) and (0 <= dx_a < n) and (0 <= dy_b < n) and (0 <= dx_b < n) and (board[dy_a][dx_a]!=1 and board[dy_b][dx_b]!=1):
                if b[0]-a[0]==0 and (visited[dy_a][dx_a][0] == 1 and visited[dy_b][dx_b][0] == 1): continue
                elif b[1]-a[1]==0 and (visited[dy_a][dx_a][1] == 1 and visited[dy_b][dx_b][1] == 1): continue
                queue = dot_check(queue,(dy_a,dx_a),(dy_b,dx_b),d)
    

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])) #7
print(solution([[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]])) #10
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]])) #21
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]])) #11
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]])) #33
print(solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])) #18


'''
<문제> 
로봇은 좌표1, 좌표2 각각이 축이되어 회전이 가능하며, 수평 또는 수직 방향으로도 이동이 가능하다.

<풀이>
BFS 이용

*일반화
로봇의 현재 위치에서 회전했을 때와, 수평 또는 수직으로 이동이 가능한 위치를 찾는다.
회전했을 때, 지나가는 대각방향의 인덱스가 벽이 존재하면 회전이 불가능하다.
수평 또는 수직으로 이동했을때도 마찬가지로 벽이 존재하면 진행이 불가능하다.
로봇이 위치하는 자리가 수평방향으로 방문했을 때와, 수직방향으로 방문했을 때가 좌표가 다르기 때문에,
방문 배열의 원소를 수평방향 방문여부, 수직방향 방문여부 두 개를 모두 기록해야한다.

<회전>
진행이 가능한 범위는 좌표1을 축으로 했을 때와, 좌표2를 축으로 했을 때 각각 수평, 수직 방향 모두 확인해야 한다.
이때, 수평인 경우, 회전 시 수직방향으로 바뀌며 이동하려는 위치의 수직 방문여부가 모두 1이라면 방문이 불가능함으로 건너뛴다.
수직인 경우, 회전 시 수평방향으로 바뀌며 이동하려는 위치의 수평 방문여부가 모두 1이라면 방문이 불가능함으로 건너뛴다.
진행이 가능하다면, 좌표1과 좌표2를 좌표의 크기 순(x1,y1<x2,y2)으로 바꿔 큐에 추가한다.

<직진>
진행이 가능한 범위는 상,하,좌,우 네 방향
수평인 상태로 진행했을 때, 이동하려는 위치의 수평 방문여부가 모두 1이라면 건너뛴다.
수직인 상태로 진행했을 떄, 이동하려는 위치의 수직 방문여부가 모두 1이라면 건너뛴다.
진행이 가능하다면, 좌표1과 좌표2를 좌표의 크기 순(x1,y1<x2,y2)으로 바꿔 큐에 추가한다.
'''