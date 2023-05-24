import sys
input = sys.stdin.readline

def solution():
    answer = 0
    result = []
    interval_sum, end = 0, 0

    for start in range(n):
        while interval_sum < s and end < n:
            interval_sum += arr[end]
            end += 1
        
        if interval_sum >= s: 
            result.append(end-start)
        interval_sum -= arr[start]

    answer = sorted(result)[0] if result else 0
    return answer

n, s = map(int, input().rstrip().split(' '))
arr = list(map(int, input().rstrip().split(' ')))

print(solution())

