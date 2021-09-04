# 3진법 변형
# 1=>1, 2=>2, 0=>4
# 몫이 3의 배수인 경우 몫-1
from collections import deque
def ternary(n):
    a_list = deque()
    while n>0:
        if n%3==0:
            a_list.appendleft('4')
            n = n//3-1
        else:
            a_list.appendleft(str(n%3))
            n//=3
    return  ''.join(a_list)
def solution(n):
    answer = ''
    answer = ternary(n)
    return answer

solution(13)