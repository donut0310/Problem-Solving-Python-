import sys
input = sys.stdin.readline


def solution():
    num = int(input())

    line, end = 0, 0
    while num > end:
        line += 1
        end += line
    
    start = end - line + 1
    gap = num - start
    
    if line % 2 == 0: # 짝수 라인
        a, b = 1, line
        a += gap
        b -= gap
        return f'{a}/{b}'

    else: # 홀수 라인
        a, b = line, 1
        a -= gap
        b += gap
        return f'{a}/{b}'
    
print(solution())