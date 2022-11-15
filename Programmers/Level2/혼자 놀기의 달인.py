from collections import deque

def solution(cards):
    answer = 0
    visited = [0] * (len(cards) + 1)
    cycle = [] # 각 사이클마다 포함되는 노드의 개수를 담은 배열    
    for card in cards:
        if visited[card]: continue
        cnt = 0 # 각 사이클에 포함되는 노드의 개수
        q = deque([card])
        
        while q:
            node = q.popleft()
            if visited[node]:
                cycle.append(cnt)
                continue
            visited[node] = 1
            cnt += 1
            q.append(cards[node - 1])
    
    if len(cycle) == 1: return 0
    cycle.sort(reverse=True)
    answer = cycle[0] * cycle[1]
    
    return answer

print(solution([8,6,3,7,2,5,1,4])) # 12

'''
<풀이>
1. 각 카드에서 시작하는 사이클을 찾는다.
2. 사이클을 찾을 때마다 사이클에 포함되는 노드의 개수를 미리 카운팅해서 배열에 담는다.
3. 사이클 배열이 1개라면 0점을 반환해야 하기 때문에 바로 리턴해준다.
4. 사이클 배열이 2개 이상이라면 가장 큰 값과 다음으로 가장 큰 값 두개를 곱해야 한다.
'''