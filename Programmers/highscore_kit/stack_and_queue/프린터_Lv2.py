from collections import deque

def solution(priorities, location):
    answer = 0
    _p = sorted(priorities)
    maxi = _p[-1]

    # 인덱스 추가
    priorities = deque(priorities)    
    for i in range(len(priorities)):
        priorities[i] = (priorities[i], i)
    
    # 프린트
    while priorities:
        tmp, index = priorities.popleft()

        if tmp == maxi:
            answer += 1
            if index == location: return answer
            _p.pop()
            maxi = _p[-1]
            
        elif tmp < maxi:
            priorities.append((tmp,index))
        
    return answer

print(solution([2, 1, 3, 2], 2))
