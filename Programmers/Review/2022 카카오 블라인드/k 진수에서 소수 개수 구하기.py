from collections import deque
import math

def convert(num: int, k: int):
    converted_num = deque()
    while num > 0:
        converted_num.appendleft(str(num % k))
        num //= k
    
    arr = []
    tmp = ''
    for i in converted_num:
        if i == '0':
            if len(tmp): arr.append(tmp)
            tmp = ''
        else: tmp += i
    if len(tmp): arr.append(tmp)
    return arr

def isprime(num: int):
    if num == 1: return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def solution(n, k):
    answer = 0
    
    nums = convert(n, k)
    
    for num in nums:
        if isprime(int(num)): answer += 1

    return answer

print(solution(437674, 3)) # 3
print(solution(110011, 10)) # 2