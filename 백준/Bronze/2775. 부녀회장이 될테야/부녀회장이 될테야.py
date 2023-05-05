import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    dp = [[0] * 15 for _ in range(15)] # 아파트 (행: 층, 열: 호)
    dp[0] = [i for i in range(15)]

    for i in range(1, 15):
        for j in range(1, 15):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    for i in range(t):
        n = int(input())
        k = int(input())
        print(dp[n][k])        

solution()