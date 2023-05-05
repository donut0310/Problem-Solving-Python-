import sys, math
input = sys.stdin.readline

def solution():
    n = int(input())
    for i in range(n):
        t = int(input())
        if t == 0: 
            print('1 0')
            continue
        elif t == 1:
            print('0 1')
            continue

        dp = [(0, 0) for _ in range(t+1)]
        dp[0] = (1, 0)
        dp[1] = (0, 1)
        
        for i in range(2, t+1):
            dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

        print(f'{dp[t][0]} {dp[t][1]}')

solution()