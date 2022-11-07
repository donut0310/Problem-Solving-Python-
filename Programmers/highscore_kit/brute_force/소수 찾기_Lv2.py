from itertools import permutations
import math

def is_prime(num):
    if num < 2: return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def solution(numbers):
    answer = 0
    p_set = set()

    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        p = permutations(numbers, i)

        for item in p:
            p_set.add(int(''.join(item)))

    for num in p_set:
        if is_prime(num): answer += 1
        
    return answer

print(solution("17")) # 3
print(solution("011")) # 2