from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    stack = deque([i for i in range(0,len(priorities))])
    a_list = deque()
    while len(set(priorities)) != 1 and len(set(priorities)) != len(priorities):
        max_v = max(priorities)
        if priorities[0] != max_v:
            priorities.append(priorities.popleft())                    
            stack.append(stack.popleft())                    
        else:
            priorities.popleft()
            a_list.append(stack.popleft())
    a_list.extend(stack)
    return a_list.index(location)+1

solution([2,1,3,2],2)
solution([1,1,9,1,1,1],0)