import sys, math
input = sys.stdin.readline

def solution():
	answer = 0
	
	n = int(input())
	if n < 3: return 0

	arr = [0]
	[arr.append(int(i)) for i in input().rstrip().split(' ')]
	
	dp = [math.inf] * (n+1)
	dp[1] = arr[1]
	dp[2] = arr[2]
	dp[3] = arr[3]
	
	for i in range(1, n+1):
		for j in range(1, 4):
			if i+j > n: continue
			dp[i+j] = min(dp[i+j], dp[i] + arr[i+j])
	
	answer = min(dp[-1], dp[-2], dp[-3])			
	return answer		
	
print(solution())

'''
최대 3칸 뛸 수 있음
독극물 최소화로 밟고 건너기

0 3 1 1 7 4 9 3
s x x o x o x x 도착
0 3 1 1
	4 4 10
	  2 8 5
	    8 5 10
		  12 14 8
		     14 8 
			 
min(dp[-1], dp[-2], dp[-3])
'''