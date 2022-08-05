from collections import defaultdict

NODE_INFO = defaultdict(list) # key = 자기 자신 노드, values = 자식 노드 리스트
MAX_G = 0 # 양의 최대 값

def dfs(animals, cur_node, next_nodes, info):
    global MAX_G
    g,w = animals[::]

    # 동물 카운트
    animal_type = info[cur_node]
    if animal_type==0: g+=1
    else: w+=1

    # 잡아 먹힌 경우
    if g-w<=0: return
    
    # 최대값 갱신
    if MAX_G < g: MAX_G = g

    # 다음 방문할 노드 탐색
    for node in next_nodes:
        _next_nodes = next_nodes[::]
        _next_nodes.remove(node)
        
        childs = NODE_INFO[node]
        _next_nodes = _next_nodes + childs
        dfs([g,w], node, _next_nodes, info)

def solution(info, edges):
    global MAX_G, NODE_INFO
    MAX_G =  0
    NODE_INFO = defaultdict(list)
    
    for i in edges:
        NODE_INFO[i[0]].append(i[1])
    
    cur_node = 0 # 시작 노드 고정
    next_nodes = NODE_INFO[cur_node]
    animals = [0,0]
    dfs(animals, cur_node, next_nodes, info)
    return MAX_G

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])) # 5
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])) # 5

'''
------------------------------------------------------------------------------------------------------------------------------------
<문제>
양의 수가 늑대 수와 같아지면 양이 모두 잡아 먹힌다.
잡아 먹히지 않는 선에서 구할 수 있는 양의 최대 수 구하기
------------------------------------------------------------------------------------------------------------------------------------
<풀이>
1. 시작 노드는 0(양) 고정
2. 시작 노드 기준 다음 진행 노드는 시작 노드의 자식 노드들로 구성
3. DFS 호출

DFS
1. 현재 노드가 양인지 늑대인지 구별 후 각각 양과 늑대를 구별하는 변수 g, w를 카운팅
2. 늑대의 수가 양의 수보다 같거나 크다면 함수 리턴
    -> 더이상 진행할 필요가 없음
    -> 재귀함수의 시작 부분으로 돌아 갔을 때, 늑대와 양의 정보는 변하지 않아야 하기에 animals 리스트를 복사하여 사용한 이유가 된다.
3. 이후, 두 변수(g, w)를 각 동물의 최대 값을 저장하는 전역 변수(MAX_G, MAX_W)와 대소 비교하여 값을 갱신
4. 현재 노드를 기준으로, 다음 진행해야할 노드들의 정보를 담은 next_nodes를 for 문을 이용해 DFS를 각각 호출한다.
5. 이때, 다음 진행해야할 노드를 DFS 호출의 현재 노드로 사용하고, 해당 노드를 기준으로 다음 진행해야할 노드를 구해서 인자로 넘겨준다.
5-1. 각각의 현재 노드들은 for문에 사용되는 next_nodes를 복사한 후, 자기 자신을 제외하고, 현재 노드의 자식 노드들을 합쳐준다.
    => _next_nodes = childs + 자신을 제외한 _next_nodes
5-2. next_nodes 리스트의 값이 없을 때까지 재귀 호출을 반복하게 되고, 이후 종료된다.
6. 데려갈 수 있는 양의 최대 값이 저장된 MAX_G를 반환
------------------------------------------------------------------------------------------------------------------------------------

'''