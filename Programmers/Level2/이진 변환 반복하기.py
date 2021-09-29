import re
from collections import deque

def binary(num):
    q = deque()
    while num>=2:
        q.appendleft(num%2)
        num//=2
    q.appendleft(num)
    return ''.join(str(i) for i in q)

def solution(s):
    cnt=0
    cnt_zero=0
    while len(s)>1:
        s_len = len(s)
        
        s = re.sub(r'0','',s)
        cnt_zero += (s_len-len(s))
        
        s = str(binary(len(s)))
        cnt+=1

    return [cnt,cnt_zero]

solution("110010101001")
# solution("01110")
# solution("1111111")