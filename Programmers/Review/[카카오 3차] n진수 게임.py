from collections import deque

def notation(n,t,m):
    d = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    s='0'
    for i in range(t*m):
        tmp = deque()
        while i:
            num = i%n
            if num<10: tmp.appendleft(str(num))
            else: tmp.appendleft(str(d[num]))
            i//=n
        s+=''.join(tmp)
    return s

def solution(n, t, m, p):
    answer = ''
    s = notation(n,t,m)
    while t:
        answer+=s[p-1]
        p+=m
        t-=1
    return answer

print(solution(2,4,2,1)) #0111
print(solution(16,16,2,1)) #02468ACE11111111
print(solution(16,16,2,2)) #13579BDF01234567

# 일정 범위의 수까지 n진법을 구해 s 변수에 모두 붙여준다.
# 튜브의 순서 p의 위치에 있는 숫자들만 뽑아서 answer 변수에 더해준다.