import sys
input = sys.stdin.readline

def solution():
	answer = 0
	
	n = int(input())
	dp = [0] * (n+1)
	
	for i in range(n):
		if i+1 <= n:
			if dp[i] == 0: dp[i+1] += 1
			else: dp[i+1] += dp[i]
		if i+3 <= n:
			if dp[i] == 0: dp[i+3] += 1
			else: dp[i+3] += dp[i]
	
	answer = dp[n] % 1000000007
	return answer

print(solution())

'''
0번째 인덱스부터 +1, +3 번 째 인덱스 까지 가는 경우의 수를 1씩 증가
+1, +3번 째 인덱스에 숫자가 존재하는 경우엔 현재 인덱스의 값과 +1, +3번 째 인덱스의 값을 누적
위와같이 하면 각 인덱스까지 올 수 있는 방법의 가짓수를 누적하는것과 같게 된다.
'''

