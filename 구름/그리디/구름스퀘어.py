import sys
input = sys.stdin.readline

def solution():
	answer = 0
	
	n = int(input())
	arr = []
	
	for i in range(n):
		s, e = map(int, input().rstrip().split(' '))
		arr.append((s, e))		
	arr.sort(key = lambda x:x[1])
	
	p_s, p_e = 0, 0
	for i in range(len(arr)):
		if i==0:
			p_s, p_e = arr[i]
		else:
			if arr[i][0] <= p_e: continue
			else:
				p_s, p_e = arr[i]
		answer += 1
		
	return answer

print(solution())

'''
각 행사가 끝나는 시간을 기준으로 오름차순 정렬한다.
각 행사들의 시작 시각이 이전 행사의 종료 시각보다 이르다면 행사가 겹치기 때문에 건너뛴다.
'''