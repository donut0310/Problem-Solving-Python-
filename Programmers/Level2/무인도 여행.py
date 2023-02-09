from collections import deque

def solution(maps):
    answer = []
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    arr = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X': arr.append([i,j])

    for i, j in arr:
        queue = deque([(i, j)])
        cnt = 0
        dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우

        while queue:
            row, col = queue.popleft()
            
            if visited[row][col]: continue
            visited[row][col] = 1
            cnt += int(maps[row][col])

            for k in range(4):
                next_y, next_x = row + dy[k], col + dx[k]
                if 0 <= next_y <= len(maps) - 1 and 0 <= next_x <= len(maps[0]) - 1 and maps[next_y][next_x] != 'X':
                    queue.append((next_y, next_x))
        if cnt: answer.append(cnt)
    
    return sorted(answer) if answer else [-1]