import sys
input = sys.stdin.readline

def solution():
    s = list(input())
    q = int(input())
    n = len(s)
    for i in range(q):
        c, l, r = input().split(' ')
        dp = [0] * (n+1)
        for j in range(int(l), int(r)+1):
            if s[j] == c: dp[j] += dp[j-1] + 1
            else: dp[j] += dp[j-1]
        print(dp[int(r)])

solution()
