import sys, heapq
input = sys.stdin.readline

n = int(input().rstrip())

def solution():
    arr = []
    for i in range(n):
        num = int(input().rstrip())
        if not num:
            if not arr: print(0)
            else: print(heapq.heappop(arr))
        else:
            heapq.heappush(arr, num)
solution()