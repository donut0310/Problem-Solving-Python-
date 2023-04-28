from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    answer = []
    max_cost = 500001
    adjlist = defaultdict(list)
    for u, v in roads:
        adjlist[u].append(v)
        adjlist[v].append(u)
    
    table = [max_cost] * (n+1)
    queue = deque([(destination, 0)])
    
    # 다익스트라
    while queue:
        node, d = queue.popleft()
        
        if d > table[node]: continue
        table[node] = d
        
        for next_node in adjlist[node]:
            if d + 1 < table[next_node]:
                queue.append((next_node, d+1))
    
    for source in sources:
        cost = table[source]
        if cost < max_cost: answer.append(cost)
        else: answer.append(-1)

    return answer