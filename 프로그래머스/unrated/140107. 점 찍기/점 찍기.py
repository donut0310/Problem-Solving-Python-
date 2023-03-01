import math

def solution(k, d):
    answer = 0
    
    arr = []
    for i in range(0, d+1, k):
        arr.append((i, int(math.sqrt(d**2 - i**2))))
    
    for x, y in arr:
        answer += y // k + 1
        
    return answer

'''
<풀이>

점과 점 사이의 거리가 d 이하를 만족!
x축 위의 점 중 최대 거리 x => root(d^2)
x 값보다 작은 정수들이 해당 x 좌표를 가지는 좌표의 최대 x 축까지의 값이 된다.
ex) d = 5 일 때, (5, 0), (4, 3), (3, 4), (2, 4), (1, 4), (0, 5)
위에서 구한 좌표들 내에 속하는 모든 점이 찍을 수 있는 점에 해당한다.
'''