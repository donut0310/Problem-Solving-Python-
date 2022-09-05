from collections import defaultdict

TREE = defaultdict(list)
MAX_G = 0

def dfs(cur_node: int, next_nodes: list, info: list, animal: list):
    global TREE, MAX_G
    g, w = animal
    animal_type = info[cur_node]

    if animal_type == 0: g += 1
    else: w += 1

    if g <= w: return
    
    if MAX_G < g: MAX_G = g

    for node in next_nodes:
        _next_nodes = next_nodes[::]
        _next_nodes.remove(node)
        _next_nodes.extend(TREE[node])
        dfs(node, _next_nodes, info, [g, w])

    return

        

def solution(info, edges):
    global TREE, MAX_G
    animal = [0, 0]
    
    for v1, v2 in edges:
        TREE[v1].append(v2)

    dfs(0, TREE[0], info, animal)
    
    return MAX_G

# print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	)) # 5
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])) # 5