import math


def solution(brown, yellow):
    answer = []

    for i in range(int(math.sqrt(yellow)), 0, -1):
        if yellow % i: continue
        
        h, w = i, yellow // i
        tmp = (w+2) * 2 + h * 2

        if tmp == brown:
            answer = [w+2, h+2]
            break

    return answer

print(solution(10, 2)) # [4, 3]