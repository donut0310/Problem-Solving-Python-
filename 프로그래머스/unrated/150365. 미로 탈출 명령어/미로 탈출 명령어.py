from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    shortest_d = abs(x - r) + abs(y - c)
    # if k < shortest_d or (k - shortest_d) % 2 != 0: return 'impossible'

    dt = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')] # d, l, r, u 사전순
    queue = deque([(x, y, '', 0)]) # 행, 열, 경로, 거리
    
    # BFS
    while queue:
        row, col, path, d = queue.popleft()
        if (row, col) == (r, c): # 도착지점 도달
            if d == k: return path # 최단거리 도달
            if (k - d) % 2 != 0: 
                # k가 5일 때 d가 4면 되돌아갔다 올 수가 없음
                # k가 5일 때 d가 3이면 되돌아갔다 올 수 있음
                return 'impossible' 
            
        for dy, dx, direction in dt:
            next_y, next_x = row + dy, col + dx
            
            if 1 <= next_y <= n and 1 <= next_x <= m:
                if abs(next_y - r) + abs(next_x - c) + d >= k: continue
                queue.append((next_y, next_x, path + direction, d + 1))
                break
    return 'impossible'