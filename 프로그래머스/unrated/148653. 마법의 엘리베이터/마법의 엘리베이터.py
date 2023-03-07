from collections import deque

def solution(storey):
    answer = 0
    costs = []
    queue = deque([(0, 0, 0, storey)]) # 누적합, 현재 스테이지의 자릿값, 오버플로우, storey
    
    while queue:
        cnt, value, overflow, storey = queue.popleft()

        if not storey:
            costs.append(cnt + overflow)
            continue
        value = storey % 10 + overflow
        storey //= 10
        queue.append((cnt + value, value, 0, storey))
        queue.append((cnt + 10 - value, 10 - value, 1, storey))
    
    answer = min(costs)
    return answer