import sys
input = sys.stdin.readline

arr = [0] * 101
dict = {}
dict[1], dict[2], dict[3] = map(int, input().split())
dict[0] = 0

last_idx = 0;
for i in range(3):
    start, end = map(int, input().split())
    arr[start] += 1
    arr[end] += -1
    last_idx = max(last_idx, end)

def solution():
    answer = 0

    for i in range(1, last_idx+1):
        arr[i] += arr[i-1]
        answer += (dict[arr[i]] * arr[i])

    return answer    

print(solution())