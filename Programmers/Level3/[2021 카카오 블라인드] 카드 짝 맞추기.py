from collections import defaultdict, deque
from itertools import permutations
import math

def search(queue, board, row, col, d):
    # 상하좌우
    up = [-1,-2,-3]
    down = [1,2,3]
    left = [-1,-2,-3]
    right = [1,2,3]
    n = len(board)

    cnt=0
    for i in range(3): # 윗 방향 조사
        nextY,nextX = row+up[i],col
        if 0<=nextY<n and 0<=nextX<n:
            if board[nextY][nextX]==0:
                if nextY==0: queue.append((nextY,nextX,d+1))
                else:
                    cnt+=1
                    queue.append((nextY,nextX,d+cnt))
            else:
                queue.append((nextY,nextX,d+1))
                cnt=0
                break

    for i in range(3): # 아래 방향 조사
        nextY,nextX = row+down[i],col
        if 0<=nextY<n and 0<=nextX<n:
            if board[nextY][nextX]==0:
                if nextY==3: 
                    queue.append((nextY,nextX,d+1))
                else:
                    cnt+=1
                    queue.append((nextY,nextX,d+cnt))
            else:
                queue.append((nextY,nextX,d+1))
                cnt=0
                break

    for i in range(3): # 왼쪽 방향 조사
        nextY,nextX = row,col+left[i]
        if 0<=nextY<n and 0<=nextX<n:
            if board[nextY][nextX]==0:
                if nextX==0: queue.append((nextY,nextX,d+1))
                else:
                    cnt+=1
                    queue.append((nextY,nextX,d+cnt))
            else:
                queue.append((nextY,nextX,d+1))
                cnt=0
                break

    for i in range(3): # 오른쪽 방향 조사
        nextY,nextX = row,col+right[i]
        if 0<=nextY<n and 0<=nextX<n:
            if board[nextY][nextX]==0:
                if nextX==3: queue.append((nextY,nextX,d+1))
                else:
                    cnt+=1
                    queue.append((nextY,nextX,d+cnt))
            else:
                queue.append((nextY,nextX,d+1))
                cnt=0
                break

def bfs(start_row, start_col, coord1, coord2, board):
    # start -> coord1
    visited1 = defaultdict(lambda:(0,0))
    queue1 = deque([(start_row, start_col, 0)])
    distance1 = math.inf
    while queue1:
        row,col,d = queue1.popleft()
        if visited1[(row,col)][0] == 1 and visited1[(row,col)][1] < d: continue
        if (row==coord1[0] and col==coord1[1]) and d < distance1: distance1 = d
        visited1[(row,col)] = (1,d)
        search(queue1, board, row, col, d)
    
    # coord1 -> coord2
    visited2 = defaultdict(lambda:(0,0))
    queue2 = deque([(coord1[0], coord1[1], 0)])
    distance2 = math.inf
    while queue2:
        row,col,d = queue2.popleft()
        if visited2[(row,col)][0] == 1 and visited2[(row,col)][1] < d: continue
        if (row==coord2[0] and col==coord2[1]) and d < distance2: distance2 = d
        visited2[(row,col)] = (1,d)
        search(queue2, board, row, col, d)

    return distance1 + distance2 + 2

def solution(board, r, c):
    answer = math.inf
    n = len(board)
    card_dict = defaultdict(list) # 각 카드별 위치 딕셔너리 key = card_num, item = card_position
    for i in range(n): 
        for j in range(n):
            if board[i][j]!=0: card_dict[board[i][j]].append((i,j))

    # 모든 카드들의 조합을 탐색 ((1,2,3), (2,3,1) ... )
    for s in permutations(range(1,len(card_dict)+1),len(card_dict)):
        _board = [i[:] for i in board]
        queue = deque([(r, c, 0)])
        tmp_distance = 0 # 각 카드 조합의 최종 거리

        for card in s:
            row,col,d = queue.popleft()
            a,b = card_dict[card]

            # 시작점으로부터 선택된 카드 한 쌍 까지의 거리를 각각 구하여 비교 후 최소값을 저장
            # start -> a -> b
            distance_a = bfs(row, col, a, b, _board)
            # start -> b -> a
            distance_b = bfs(row, col, b, a, _board)

            if distance_a < distance_b: 
                queue.append((b[0], b[1], d + distance_a))
                tmp_distance = d + distance_a
            else: 
                queue.append((a[0], a[1], d + distance_b))
                tmp_distance = d + distance_b
            # 카드 뒤집기
            _board[a[0]][a[1]] = 0
            _board[b[0]][b[1]] = 0
        if tmp_distance < answer: answer = tmp_distance # 최소 거리
    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)) # 14
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1)) # 16
print(solution([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0)) # 32

'''
<풀이>
1. 카드 번호들을 조합하여 모든 순열을 구한다. (1,2,3), (2,3,1) ...
2. 각 순열마다 시작점 (r,c) 에서 순서대로 카드번호까지의 거리를 구한다.
2-1. 이때, 각 카드는 모두 2쌍으로 이루어져 있기 때문에,
     거리 1: 시작점 -> 카드 A-a 까지의 거리 + 카드 A-a -> 카드 A-b 까지의 거리와
     거리 2: 시작점 -> 카드 A-b 까지의 거리 + 카드 A-b -> 카드 A-a 까지의 거리를 모두 구한다.
2-2. 거리를 구할 때, 한 칸 도약과, ctrl 도약의 거리를 주의하여 계산한다.
2-3. 거리 1과 거리 2 중 최소값을 tmp_distance 값에 저장한 뒤, 시작점의 위치를 갱신한다.
3. 각 순열의 모든 원소를 위 과정을 반복한다.

핵심은 시작점에서 선택해야할 모든 카드번호의 조합을 구해야하며,
이때, 선택된 카드의 쌍 중에 어떤 카드를 선택할지, 두 카드까지의 거리를 모두 계산 후,
더 가까운 쪽의 카드를 선택하는 과정을 반복해야 한다.

'''