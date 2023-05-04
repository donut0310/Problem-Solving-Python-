import sys
input = sys.stdin.readline

def solution():
	answer = 0
	
	k = int(input())
	arr = [0] * 100001
	arr[1] = 0
	arr[2] = 1
	
	for i in range(3, k+1):		
		arr[i] = arr[i-1] + arr[i-2]
	
	answer = arr[k] % 1000000007
	return answer

print(solution())