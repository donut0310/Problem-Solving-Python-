from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1, queue2 = deque(queue1), deque(queue2)
    
    s = sum(queue1)
    mid = (s + sum(queue2)) // 2
    
    while queue1 and queue2:
        if s == mid: return answer
        elif s < mid:
            queue1.append(queue2.popleft())
            s += queue1[-1]
        else:
            s -= queue1.popleft()
        answer += 1
        
    return -1