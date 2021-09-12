# stack
from collections import deque

def solution(s):
    s = deque(s)
    stack = deque(s.popleft())

    while len(s)>0:
        if len(stack)==0:
            stack.append(s.popleft())
            continue
        
        a = stack.pop()
        b = s.popleft()
        if not (a=='(' and b== ')'):
            stack.extend([a,b])
    
    if len(stack)>0:
        return False
    return True

solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")