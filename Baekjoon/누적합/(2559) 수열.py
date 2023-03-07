import sys

input = sys.stdin.readline 

def solution():
    n, k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    dp = [0] * (n+1)
    
    # 누적합
    for i in range(1, n+1):
        dp[i] = arr[i-1] + dp[i-1]

    answer = -100 * k - 1
    for i in range(k, n+1):
        answer = max(dp[i] - dp[i-k], answer)
    print(answer)

solution()

'''
<풀이>
전체 구간합을 구한 뒤 k 번째 인덱스(i) 부터 i-k번째 인덱스까지의 구간합을 빼주면서
최대값을 갱신한다.
'''