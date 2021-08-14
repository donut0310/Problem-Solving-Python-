from collections import deque
import math

def ternary(n):
    queue = deque()
    while n>=3:
        queue.append(n%3)
        n//=3
    queue.append(n)
    return queue

def solution(n):
    answer = 0
    index=0
    queue = ternary(n)

    for i in reversed(range(len(queue))):
        answer+=int(queue[index]*math.pow(3,i))
        index+=1
    return answer

solution(45)
solution(125)