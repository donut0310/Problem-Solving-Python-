from collections import deque
import math

def make(n,k):
    str_num = ''
    while n>0:
        str_num+=(str(n%k))
        n//=k
    return str_num[::-1]

# 첫번째 풀이 => 시간 복잡도 불통
def is_prime(num):
    if num==1: return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

# 두번째 풀이 => 시간 복잡도 통ㅘ
def is_prime(num):
    if num==1: return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def solution(n, k):
    num = make(n,k)
    cnt=0
    tmp =''
    for i in range(len(num)):
        if num[i]=='0' and len(tmp)!=0:
            tmp=int(tmp)
            if is_prime(tmp):
                cnt+=1
            tmp=''
            continue
        elif num[i]=='0' and len(tmp)==0:
            continue
        tmp+=num[i]
        if i==len(num)-1 and len(tmp)>0:
            tmp=int(tmp)
            if is_prime(tmp):
                cnt+=1
    return cnt

print(solution(437674,3))
print(solution(110011,10))
print(solution(1000,2))

# 첫번째 풀이 시 소수 판별에 있어서 2~판별 할 수 까지를 범위로 잡았더니 시간 복잡도에서 불통하였다.
# 소수 판별 방식에서 에라토스테네스의 체를 응용해 최대 판별 범위를 판별 할 수까지로 잡는게 아니라
# 판별 할 수의 제곱근 값까지만 범위를 잡아도 제곱근 값이 판별할 수의 인수가 되는지 안되는지를 판별할 수 있다.
# 따라서 두번째 풀이 시 판별 범위를 2~ 판별할 수의 제곱근 값까지 반복문을 돌렸더니 시간 복잡도에서 통과하였다.
