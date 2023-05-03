from collections import deque
import sys
input = sys.stdin.readline


def solution():
    answer = 0
    word = deque(list(input().rstrip()))
    dist = {'c=': 1, 'c-': 1, 'dz=': 1, 'd-': 1, 'lj': 1, 'nj': 1, 's=': 1, 'z=': 1}

    while word:
        tmp = ''
        for i in range(3):
            if word:
                tmp += word.popleft()
        
        while len(tmp) > 1:
            if tmp in dist.keys(): 
                answer += 1
                tmp = ''
            else: 
                word.appendleft(tmp[-1])
                tmp = tmp[:-1]

        if len(tmp) == 1: answer += 1
        
    return answer
   
print(solution())