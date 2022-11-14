from collections import deque

def solution(order):
    answer = 0
    q = deque([i for i in range(1, len(order) + 1)])
    s = []
    
    for box in order:
        if s and s[-1] == box:
            s.pop()
            answer += 1
            continue
        
        while q and q[0] != box:
            s.append(q.popleft())
        
        if q:
            q.popleft()
            answer += 1
        else: break
    return answer

print(solution([4, 3, 1, 2, 5])) # 2

'''
<풀이>
order 순서대로 박스를 찾아야한다.
1. 컨베이어 벨트의 첫번째 박스가 선택해야할 박스가 아니라면 보조 컨테이너 벨트로 넘긴다.
2. 보조 컨테이너 벨트에 선택해야할 박스가 있다면 보조 컨테이너 벨트에서 제거한다.
3. 보조 컨테이너 벨트에 선택해야할 박스가 없고, 컨베이어 벨트의 첫번째 박스가 선택해야할 박스라면 컨베이어 벨트에서 제거한다 popleft

'''
