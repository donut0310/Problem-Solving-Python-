from collections import deque

def bfs(q, i):
    tmp = deque([])
    while q:
        n = q.popleft()
        tmp += [n+i, n-i]
    return tmp

def solution(numbers, target):
    answer = 0
    q1, q2 = deque([numbers[0]]), deque([-numbers[0]])
    
    for i in range(1, len(numbers)):
        q1 = bfs(q1, numbers[i])
        q2 = bfs(q2, numbers[i])

    answer = q1.count(target) + q2.count(target)
    return answer