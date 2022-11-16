import math

def gcd(num, arr):
    tmp = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0: tmp.extend([num // i, i])
    tmp = sorted(tmp, reverse=True)

    for num in tmp:
        cnt, result = 0, 0
        for item in arr:
            if item % num != 0: break
            else: cnt += 1
        if cnt == len(arr):
            result = num
            break
    return result
        

def calculate(arr, target):
    for num in arr:
        if num % target == 0: return 0
    return target

def solution(arrayA, arrayB):
    answer = 0
    min_a, min_b = min(arrayA), min(arrayB)
    target_a, target_b = gcd(min_a, arrayA), gcd(min_b, arrayB)

    a = calculate(arrayB, target_a)
    b = calculate(arrayA, target_b)

    answer = max(a,b)
    return answer

print(solution([10, 17], [5, 20])) # 0
print(solution([10, 20], [5, 17])) # 10
print(solution([14, 35, 119], [18, 30, 102])) # 7

'''
<풀이>
A 배열의 모든 수를 나눌 수 있는 수 중에서 가장 큰 수가 B 배열의 모든 수를 나누지 못하는 경우를 찾아야한다.
즉, A 배열의 최대 공약수가 B 배열을 모두 나누지 못하는 경우를 찾아야 한다.
만일 A 배열의 최대 공약수가 B 배열의 원소 중 하나라도 나눌 수 있다면 0(조건에 만족하는 수가 없음)을 의미한다..
위를 만족하는 각 배열에서의 최대값중 큰 값을 반환하면 된다.
'''