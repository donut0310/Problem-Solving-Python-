import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = [0]
    [arr.append(int(input())) for i in range(n)]
    
    if n < 2: return arr[n]
    
    dp = [0] * (n+1)
    dp[1] = arr[1]
    dp[2] = max(arr[2], arr[1] + arr[2])
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    return dp[n]

print(solution())

'''
문제 조건, 연속된 3개의 계단은 밟으면 안된다를 만족하기 위해선
i-2 번째에서 2칸을 오른 경우와, 
i-3번째 계단까지 올랐을 때의 누적합과 이후 2칸을 오르고 1칸을 올랐을 때의 경우로 나눠 생각해야한다.
(1칸 오르고 2칸을 올랐을 때는 1칸을 오르기 전 연속된 두 계단은 올라왔을 수도 있기 때문!)

위 두 경우 중 더 큰 값을 현재 계단까지 올랐을 때의 누적합으로 갱신하는 점화식을 이용한다.
 => dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
'''