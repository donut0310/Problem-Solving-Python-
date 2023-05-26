import sys
input = sys.stdin.readline

def solution():
    answer = 0
    start, end = 1, coord[-1] - coord[0]

    if c == 2: return end

    while start < end:
        mid = (start + end) // 2
        cnt = 1
        last_idx_of_c = coord[0]

        for i in range(n):
            if coord[i] - last_idx_of_c >= mid:
                cnt += 1
                last_idx_of_c = coord[i]
        
        if cnt < c:
            end = mid
        else: 
            answer = mid
            start = mid + 1
    return answer

n, c = map(int, input().rstrip().split(' '))
coord = [int(input()) for _ in range(n)]
coord.sort()

print(solution())

'''
1. 집들 간의 거리를 이분탐색의 재료로 써야함
start = 1, end = 마지막집 - 첫번째 집, mid = (start + end) // 2

2. 첫 번째 집에 공유기를 설치한다고 가정하고, 두번째 집부터 마지막으로 설치된 공유기(여기선 첫번째 집) 까지의
    거리가 mid보다 크거나 같다면 새로운 공유기를 설치하고 마지막으로 설치된 공유기의 위치를 갱신!

3. 모든 공유기를 설치했을 때 조건에 주어진 공유기 수보다 적다면 간격을 줄여야함
    end에 mid 대입

4. 설치된 공유기가 주어진 공유기 수보다 크거나 같다면 간격을 다시 넓혀야함
    start = mid + 1


1 2 4 8 9
s = 1, e = 9-1 => 8, m = 4
cnt = 1, t = 1
i=1: 2 - 1 < 4
i=2: 4 - 1 < 4
i=3: 8 - 1 > 4
    t = 3
    cnt = 2
i=4: 9 - 8 < 4
cnt < 3
    s = 1
    e = 4
    m = 2

'''