import sys
input = sys.stdin.readline

def solution():
	p1, p2 = 0, 0
	t = int(input())
	arr = list(map(int, input().rstrip().split(' ')))
	
	for i in arr:
		if i%2 != 0: p1 += 1
		else: p2 += 1
	
	if p1 > p2: return p1
	elif p1 < p2: return p2
	else: return 'tie'

print(solution())

'''
사탕은 무조건 p1이 먼저 가져간다.
한 번에 가져갈 수 있는 개수는 1 or 3
위 조건을 만족할 때 p1이 이기는 경우는 사탕의 개수가 홀수 일 때만 성립한다.
'''