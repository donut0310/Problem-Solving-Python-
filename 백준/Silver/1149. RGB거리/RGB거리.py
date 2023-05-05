import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dp = [[0] * 4 for _ in range(n+1)]

    for i in range(1, n+1):
        r, g, b = map(int, input().rstrip().split(' ')) 

        dp[i][1] = min(dp[i-1][2], dp[i-1][3]) + r
        dp[i][2] = min(dp[i-1][1], dp[i-1][3]) + g
        dp[i][3] = min(dp[i-1][1], dp[i-1][2]) + b        
    
    return min(dp[-1][1:])

print(solution())