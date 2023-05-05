import sys
input = sys.stdin.readline

def solution():
	answer = 0
	n = int(input())
	
	if n >= 40:
		answer += n // 40
		n %= 40
	if n >= 20:	
		answer += n // 20
		n %= 20
	if n >= 10:
		answer += n // 10
		n %= 10
	if n >= 5:
		answer += n // 5
		n %= 5
	if n >= 1:
		answer += n // 1
		n %= 1
		
	return answer

print(solution())