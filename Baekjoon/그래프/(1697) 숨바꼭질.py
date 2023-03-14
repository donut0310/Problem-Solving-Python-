from collections import deque
import sys

input = sys.stdin.readline

start, end = map(int, input().split(' '))

def solution():
    queue = deque([(start, 0)])
    visited = [0] * 100001

    while queue:
        p, cnt = queue.popleft()

        if visited[p]: continue
        visited[p] = 1

        if p == end: 
            print(cnt)
            break

        dx = [p + 1, p - 1, p * 2]
        for i in dx:
            if 0 <= i <= 100000 and not visited[i]:
                queue.append((i, cnt+1))    

solution()

'''
<풀이>
1. 각각의 위치마다 움직일 수 있는 거리는 +1, -1 *2 3가지다
2. bfs를 이용해 현재 위치에서 움직일 수 있는 거리 중 방문하지 않은 위치들만 큐에 추가하면서
    탐색하다 end 위치에 도달하면 종료한다.
'''