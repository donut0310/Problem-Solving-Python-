import sys
input = sys.stdin.readline

def solution():
	answer = 0
	n = int(input())
	arr = [0] * 31
	arr[1] = 3
	
	for i in range(2, n+1):
		arr[i] = arr[i-1] * 3
	
	for i in range(n+1):
		answer += arr[i]
		
	return answer

print(solution())

'''
2, 3, 6으로만 구성되어야 재원넘버가 된다.
1의 자리: 2, 3, 6 => 3
10의 자리: 22, 23, 26, 32, 33, 36, 62, 63, 66 => 9
100의 자리: 222, 223, 226, 232, 233, 236, 262, 263, 266, ... => 9*3 = 27
1000의 자리: 2222, 2223, 2226, 2232, 2333, 2336, 2262, 2263, 2266 ... => 27 * 3 = 81
'''