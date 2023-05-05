import sys, math
input = sys.stdin.readline

def solution():
    n = int(input())

    if n < 6: return 1 if n==3 or n==5 else -1

    dp = [math.inf] * (n+1)
    dp[3] = 1
    dp[5] = 1

    for i in range(6, n+1):
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    
    return dp[n] if dp[n] < math.inf else -1

print(solution())