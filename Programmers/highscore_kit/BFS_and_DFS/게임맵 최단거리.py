from collections import deque
    
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0, 1)]) # x, y, d
    visited = [[0] * m for _ in range(n)]
    maps[n-1][m-1] = -1
    
    while queue:
        x, y, d = queue.popleft()
        if visited[x][y]: continue
        maps[x][y] = d
        visited[x][y] = 1
        
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] and not visited[next_x][next_y]:
                queue.append((next_x, next_y, d+1))

    answer = maps[n-1][m-1]
    return answer