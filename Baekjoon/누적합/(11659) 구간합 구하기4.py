import sys

input = sys.stdin.readline # 이렇게 안하면 값 입력받을 때 시간초과뜸

def solution():
    n, m = map(int, input().split())

    arr = list(map(int, input().split(' ')))
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] += arr[i-1] + dp[i-1]

    for _ in range(m):
        a, b = map(int, input().split(' '))
        print(dp[b] - dp[a-1])

solution()