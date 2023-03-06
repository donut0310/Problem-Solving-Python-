from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    dt = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')] # d, l, r, u 사전순
    queue = deque([(x, y, '', 0)]) # 행, 열, 경로, 거리
    
    # BFS
    while queue:
        row, col, path, d = queue.popleft()
        if (row, col) == (r, c): # 도착 지점 도달
            if d == k: return path # 최단 거리로 도착지점 도달하는 경우
            if (k - d) % 2 != 0: 
                # ex.1) k가 5일 때 d가 4면 되돌아갔다 올 수가 없음
                # ex.2) k가 5일 때 d가 3이면 되돌아갔다 올 수 있음
                return 'impossible' 
            
        for dy, dx, direction in dt:
            next_y, next_x = row + dy, col + dx
            
            if 1 <= next_y <= n and 1 <= next_x <= m:
                # 다음 지점에서 도착 지점까지의 거리와 현재까지 온 거리의 합이 k 보다 크거나 같다면 갈 필요가 없다. 즉, 사전순서상 위쪽보단 아래쪽, 오른쪽보단 왼쪽을 먼저 탐색하게 되는데 이 경우에 어느쪽이 최단거리로 가는 좌표인지를 결정해야만 한다.
                if abs(next_y - r) + abs(next_x - c) + d >= k: continue
                queue.append((next_y, next_x, path + direction, d + 1))
                break
    return 'impossible'

'''
<풀이>
출발지점에서 도착지점까지 k 값만큼 움직여서 갈 수 있는 경로 중 사전순으로 가장 빠른 길을 찾아야 한다.
이는 사전순이기 때문에 각 좌표에서 4방향으로 움직일 때(상하좌우(u, d, l, r)) 우선순위가 존재함을 알 수 있다. => d, l, r, u

bfs를 이용해 각 좌표에서 4방향(d, l, r, u)을 순서대로 탐색하며 갈 수 있는 방향을 고르면 정답을 구할 수 있는데, 이때 서로 대응되는 방향(상<->하, 좌<->우) 중 에서 우선순위를 구해야한다.

각 방향을 탐색할 때, 현재까지 온 거리 + 다음 좌표에서 도착지점까지의 거리의 값이 k 보다 크거나 같다면 대응되는 방향이 도착지점까지 더 가깝다는게 보장되기 때문에 조건문을 추가해서 방향을 선택한다.

방향을 정했다면 나머지 3방향은 갈 필요가 없기 때문에 선택한 다음 좌표의 정보를 큐에 담고 break로 반복문을 종료한다.
'''