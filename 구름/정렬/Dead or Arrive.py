# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import defaultdict

def solution():
	answer = 0
	n = int(input())
	cars = defaultdict(tuple)

	for i in range(1, n+1):
		v, w = map(int, input().split(' '))		
		if not cars[v]: cars[v] = (i, w)
		else:
			c_v, c_w = v, cars[v][1]
			if c_v == v and c_w == w: cars[v] = (i, w) # 속도와 내구도가 모두 같으면 번호가 큰 차량 선택
			elif c_v == v and c_w < w: cars[v] = (i, w)

		
	for v in cars:
		answer += cars[v][0]
		
	return answer

print(solution())

'''
각 차량 속도 v, 내구도 w
속도가 다르면 부딪침 없이 결승선에 들어온다.
속도가 같은 차량이 여러 대 있다면 그 중 내구도가 가장 높은 차량만 결승선에 들어온다.
속도와 내구도가 모두 같은 차량이 여러 대 있다면, 그 중 번호가 가장 큰 차량만 결승선에 들어온다.

'''