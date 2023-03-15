import sys, heapq, math

input = sys.stdin.readline
n, k = map(int, input().split(' ')) # 수빈이와 동생의 위치

def solution():
    table = [math.inf] * 100001
    queue = [(0, n)] # 거리, 위치
    table[n] = 0 # 시작점 거리 초기화 필수!!

    while queue:
        d, location = heapq.heappop(queue)
        if d > table[location]: continue

        if location == k:
            print(table[location])
            break

        dx = [(1, location + 1), (1, location - 1), (0, location * 2)]
        for w, next_location in dx:
            if 0 <= next_location <= 100000:
                cost = w + d
                if cost < table[next_location]:
                    table[next_location] = cost
                    heapq.heappush(queue, (cost, next_location))

solution()

'''
<풀이>
다익스트라의 응용으로 풀 수 있는 문제다.
매 반복마다 움직일 수 있는 지점 3곳 location - 1, location + 1, location * 2마다 각각 소요되는 시간을 튜플로 저장한 뒤 dx 배열에 넣는다.
위에서 지정한 3 곳의 위치가 0 ~ 100000 범위 내에 있는 경우에만 큐에 힙푸시를 해주면 된다.
처음으로 location 값이 k위치가 되는 경우 최단거리가 보장되기 때문에 출력하고 종료한다.
'''