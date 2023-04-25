from collections import defaultdict

MAX = 51
matrix = [[0] * MAX for _ in range(MAX)]
table = defaultdict(tuple)
merge_table = defaultdict(list)


def find(coord):
    global table
    if table[coord] == coord: return coord
    else: return find(table[coord])

def union(coord1, coord2):
    global matrix, table, merge_table
    
    p1 = find(coord1)
    p2 = find(coord2)
    if p1 == p2: return
    coord_order = sorted([p1, p2], key = lambda x:(x[0], x[1]))[0]
    
    # 좌표 병합
    if coord_order == p1: 
        table[p2] = p1
        merge_table[p1] = list(set(merge_table[p1] + merge_table[p2]))
        merge_table[p2] = [p2]
    else: 
        table[p1] = p2
        merge_table[p2] = list(set(merge_table[p1] + merge_table[p2]))
        merge_table[p1] = [p1]

    # 값 병합
    value1, value2 = matrix[coord1[0]][coord1[1]], matrix[coord2[0]][coord2[1]] 
    if (value1 and value2) or (value1 and not value2): update_current_cell(coord2, value1)
    elif value2 and not value1: update_current_cell(coord1, value2)


def update_current_cell(coord, value):
    global matrix, table, merge_table
    # 현재 셀의 부모 노드를 찾는다.
    p = find(coord)

    # 병합 정보를 저장한 dict에서 부모 노드에 속하는 모든 자식 노드들의 값을 갱신한다.
    for r, c in merge_table[p]:
        matrix[r][c] = value


def update_all_a_with_b(value1, value2):
    global matrix
    for i in range(1, MAX):
        for j in range(1, MAX):
            if matrix[i][j] == value1:
                matrix[i][j] = value2 # 값 변경

def merge(r1, c1, r2, c2):
    union((r1, c1), (r2, c2))

def unmerge(r, c):
    global table, merge_table
    # 현재 셀의 부모 노드를 찾는다.
    p = find((r, c))

    # 현재 셀의 모든 병합을 해제한다. 값이 있다면 r, c 좌표가 그 값을 가져가고 나머지 좌표는 값을 초기화 해야한다.
    value = matrix[r][c]

    while merge_table[p]:
        coord = merge_table[p].pop() # 병합 해제
        table[coord] = coord # 셀의 부모 노드를 자기 자신으로 초기화
        matrix[coord[0]][coord[1]] = 0 # 값 초기화
    merge_table[p] = [p]
    if value: matrix[r][c] = value

def solution(commands):
    answer = []
    global matrix, table, merge_table

    for i in range(1, MAX):
        for j in range(1, MAX):
            table[(i,j)] = (i,j)
            merge_table[(i,j)] = [(i,j)]

    for cmd in commands:
        cmd = cmd.split(' ')
        if cmd[0] == "UPDATE":
            if len(cmd) == 4: update_current_cell((int(cmd[1]), int(cmd[2])), cmd[3])
            else: update_all_a_with_b(cmd[1], cmd[2])
        elif cmd[0] == "MERGE": merge(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
        elif cmd[0] == "UNMERGE": unmerge(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "PRINT":
            if matrix[int(cmd[1])][int(cmd[2])]: answer.append(matrix[int(cmd[1])][int(cmd[2])])
            else: answer.append("EMPTY")
            
    return answer

'''
<풀이>
병합된 셀들의 연결 정보를 저장하기 위해서 union-find 알고리즘을 사용한다.

부모 노드 좌표를 저장할 table dict 선언
각 셀마다 자식노드들의 정보를 기록할 merge_info dict 선언
각 셀마다 값을 저장하기 위해 matrix 선언

1. update를 할 때는 해당 셀이 병합된 셀일 수도 있기 때문에
부모 좌표를 찾아 해당 부모좌표에 속하는 모든 자식 좌표들의 값까지 모두 변경해주어야 한다.
2. merge를 할 때는 해당 셀과 타겟이 되는 셀이 각각 병합된 셀일 수도 있기 때문에
부모 좌표를 찾아 서로를 연결해주어야 하며 이때 값 정보의 갱신 역시 조건에 맞게 모든 좌표에 적용되어야 한다.
3. unmerge를 할 때는 해당 셀의 부모좌표를 찾은 후 부모 좌표에 속하는 모든 자식 좌표들과의 병합 관계를
해제해주어야 한다.
'''