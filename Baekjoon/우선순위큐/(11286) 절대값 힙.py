import sys, heapq

input = sys.stdin.readline

n = int(input().rstrip())

def solution():
    arr = []
    for _ in range(n):
        num = int(input().rstrip())
        if num: heapq.heappush(arr, (abs(num), num))
        else:
            if arr: print(heapq.heappop(arr)[1])
            else: print(0)
                    
solution()
