import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
matrix = []
visited = [[[0] * 2 for _ in range(m) ] for _ in range(n)] # 벽을 안뚫고 온 거리, 벽을 뚫고 온 거리

for i in range(n):
    matrix.append(list(map(int, input().rstrip())))

def solution():
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([(0, 0, 0, 1)]) # row, col, flag, cnt
    visited[0][0][0] = 1

    while queue:
        row, col, flag, cnt = queue.popleft()
        if row == n-1 and col == m-1: 
            print(visited[n-1][m-1][flag])
            return

        for i in range(4):
            next_y, next_x = row + dy[i], col + dx[i]
            if 0 <= next_y < n and 0 <= next_x < m:
                if matrix[next_y][next_x] == 0 and not visited[next_y][next_x][flag]: # 벽이 아닐 때 아직 방문하지 않았다면
                    visited[next_y][next_x][flag] = cnt + 1
                    queue.append((next_y, next_x, flag, cnt + 1))
                elif matrix[next_y][next_x] == 1 and not flag: # 벽을 만났을 때 지금까지 부순 적이 없는 경우
                    visited[next_y][next_x][1] = cnt + 1
                    queue.append((next_y, next_x, 1, cnt + 1))
    print(-1)

solution()

'''
<풀이>
벽을 부술 수 있는 회수는 총 1회
벽을 부수고 지나왔는지, 안부수고 지나왔는지 2개를 각각 기록해야한다.
따라서 방문 정보를 저장할 배열을 3차원으로 구성해 2개의 정보를 각각 기록해야한다. => [0, 0] -> 벽을 부수지 않고 진행, 벽을 부순 뒤 진행
3차원 배열을 만들 때 주의해야할 점은 [0] * 2 를 총 m열의 개수만큼 반복해주어야 한다는 것!
[0, 0]을 m열의 개수만큼 반복하는것은 3차원 배열로 접근이 불가능하다...
이와같이 만들어 준 후에 matrix의 각 행열에서 다음으로 진행할 칸을 탐색해야한다.
이때, 다음 행선지가 벽이 아니면서 아직 방문하지 않은 경우, 다음 행선지가 벽인데 지금까지 벽을 부수고 온 적이 없는 경우
이 두가지가 다음 행선지를 고를 수 있는 조건이 된다.
첫 번째 경우는 벽이 아닌 경우 이미 벽을 부수고 왔을 수도 있고, 벽을 부순 적이 없을 수도 있기 때문에 
3차원 배열에 접근할 때 flag를 통해서 이전에 부수고 온 적이 있고 없고의 값으로 접근해야 한다. 
두 번째 경우는 하나의 경우만 존재하므로 3차원 배열의 인덱스를 1로 지정해서 탐색하면 된다.
'''