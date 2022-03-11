import math

def notation(n,k):
    num=''
    while n>0:
        mod=divmod(n,k)
        n=mod[0]
        num+=str(mod[1])
    return num[::-1]

def is_prime(num):
    if num == 1: return 0
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0: return 0
    return 1

def solution(n, k):
    answer = 0
    num = notation(n,k) # 진법 변환
    start, end = 0, len(num)
    # 소수 판별
    cnt=0
    for i in range(end):
        if num[i] == '0':
            if cnt==0: continue
            answer += is_prime(int(num[start:i]))
            start = i+1
            cnt=0
        elif i == end-1: answer += is_prime(int(num[start:]))
        else: cnt+=1
    return answer


print(solution(437674,3)) # 3
# print(solution(110011,10)) # 2
# print(solution(110052,10))

# notation 함수를 통해 주어진 수에 대하여 k 진법으로 변환한다. 
# 이후 변환된 수를 조건에 맞게 분리한 후 is_prime 함수를 통해 소수인지 아닌지 판별한다.
# 조건에 맞게 분리된 임의의 수 x가 소수인지 판별할 때 수의 성질을 이용해 2~x-1 까지 모든 수로 나누는게 아니라
# 특정한 수의 제곱근 값까지만 비교한다.
