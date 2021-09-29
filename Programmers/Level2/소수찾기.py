# Brute Force
from itertools import permutations

def isdecimal(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
        if cnt>2:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)

    p, set_p=[], []

    [p.extend(permutations(numbers,i)) for i in range(1,len(numbers)+1)]
    p=list(set(p))

    for i in p:
        set_p.append(int(''.join(i)))
    set_p=list(set(set_p))

    for i in set_p:
        if i==0 or i==1:continue
        if isdecimal(int(i)):
            answer+=1
    return answer

solution('17')
solution('011')