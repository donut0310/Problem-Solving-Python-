import math
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(int(math.sqrt(total)),0,-1):
        if total%i==0:
            if (total//i-2) * (i-2) != yellow: continue
            answer=[total//i,i]
            break
    return answer

'''
<풀이>
전체 타일 개수를 구한 후 가로와 세로 길이가 될 수 있는 값을 찾는다.
이때 가로와 세로길이에서 각각 2를 뺀 값 -> 노란색 타일의 가로와 세로값이 되어야함으로 해당 조건을 만족하는 값을 찾는다.
'''