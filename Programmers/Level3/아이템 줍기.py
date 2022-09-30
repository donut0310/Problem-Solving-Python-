from collections import deque
import math

def bfs(cx, cy, ix, iy, matrix):
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    dist = [[math.inf] * 102 for _ in range(102)]
    queue = deque([(cx * 2, cy* 2, 1)])

    while queue:
        row, col, d = queue.popleft()
        for i in range(4):
            nextX, nextY = row + dx[i], col + dy[i]
            if 0 <= nextX < 102 and 0 <= nextY < 102 and matrix[nextX][nextY] == 1:
                if d + 1 < dist[nextX][nextY]:
                    dist[nextX][nextY] = d + 1
                    queue.append((nextX, nextY, d + 1))

    return dist[ix*2][iy*2]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    matrix = [[2] * 102 for _ in range(102)] 
    # 정 사이즈로 하면, 칸이 겹치는 경우가 발생한다. 
    # 예제 1번의 경우 (3,5) -> (3,6) 의 길이는 3이어야 하는데, 두 좌표는 인접해있기 때문에 최단 경로로 +1이 되어버린다.
    # 따라서, 배열을 사이즈 2배로 키워서 좌표간에 인접하지 않도록 변경해야한다.
    
    for r1, c1 ,r2, c2 in rectangle:
        for i in range(r1 * 2, r2 * 2 + 1):
            for j in range(c1 * 2, c2 * 2 + 1):
                if i == r1 * 2 or i == r2 * 2 or j == c1 * 2 or j == c2 * 2:
                    if matrix[i][j] == 2: matrix[i][j] = 1 # 다른 사각형의 내부가 아닌 경우에만 테두리를 표시
                else: 
                    matrix[i][j] = 0
    answer = bfs(characterX, characterY, itemX, itemY, matrix)
    return answer // 2

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)) # 11