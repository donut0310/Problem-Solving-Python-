import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())

arr = []
[heappush(arr, i) for i in map(int, input().split(' '))]

def solution():
    answer = 0
    t = 0
    while arr:
        tmp = heappop(arr)
        answer += t + tmp
        t += tmp
    print(answer)

solution()