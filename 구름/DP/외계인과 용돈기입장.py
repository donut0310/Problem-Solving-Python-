import sys
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split(' '))
	info = input().rstrip().split(' ')
	arr = [0] * (n+1)
	
	
	for i in range(len(info)):
		if info[i][0] == '+':
			arr[i+1] = int(info[i][1:])
		else:
			arr[i+1] = -int(info[i][1:])
	
	for i in range(1, n+1):
		arr[i] += arr[i-1]
	
	for i in range(m):
		start, end = map(int, input().split(' '))
		acc_sum = arr[end] - arr[start-1]
		print(f'+{acc_sum}') if acc_sum > 0 else print(f'{acc_sum}')
		
solution()