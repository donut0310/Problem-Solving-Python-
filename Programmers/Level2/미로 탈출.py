import heapq, math

def bfs(maps, start, end, row, col):
    queue = [start]
    dist = [[math.inf] * col for _ in range(row)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        r, c, d = heapq.heappop(queue)
        if d >= dist[r][c]: continue
        dist[r][c] = d
        
        for i in range(4):
            next_y, next_x = r + dy[i], c + dx[i]
            if 0 <= next_y < row and 0 <= next_x < col and maps[next_y][next_x] != 'X':
                heapq.heappush(queue, (next_y, next_x, d+1))
                
    distance = dist[end[0]][end[1]]
    return distance

def solution(maps):
    answer = 0
    row, col = len(maps), len(maps[0])    
    
    s, l, e = None, None, None
    
    for i in range(row):
        maps[i] = list(maps[i])
        
        for j in range(col):
            if maps[i][j] == 'S': s = (i, j, 0)
            if maps[i][j] == 'L': l = (i, j, 0)
            if maps[i][j] == 'E': e = (i, j, 0)
        
    answer = bfs(maps, s, l, row, col) + bfs(maps, l, e, row, col)
    return answer if answer != math.inf else -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1

'''
<풀이>
1. S -> L 최단거리
2. L -> E 최단거리
3. (1) + (2)
'''