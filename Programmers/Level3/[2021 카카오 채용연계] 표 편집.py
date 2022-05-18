def clear_col(d, stack:list, dict_stack: dict, k):
    stack.append(k)
    dict_stack[k] = 1
    prev, next = d[k]
    if prev == None: # 첫 행인 경우 다음 노드의 이전 노드는 None
        d[next][0] = None
        k = next
    elif next == None: # 마지막 행인 경우 이전 노드의 다음 노드는 None
        d[prev][1] = None
        k = prev
    else:
        d[prev][1] = next
        d[next][0] = prev
        k = next
    return k

def reset_col(d, stack:list, dict_stack: dict):
    idx_to_reset = stack.pop()
    dict_stack[idx_to_reset] = 0

    if d[idx_to_reset][0] == None: # 첫 행인 경우 다음노드의 이전 노드를 첫 행의 번호로 바꾼다.
        d[d[idx_to_reset][1]][0] = idx_to_reset
    elif d[idx_to_reset][1] == None: # 마지막 행인 경우 이전 노드의 마지막 노드를 마지막 행의 번호로 바꾼다.
        d[d[idx_to_reset][0]][1] = idx_to_reset
    else:
        d[d[idx_to_reset][0]][1] = idx_to_reset
        d[d[idx_to_reset][1]][0] = idx_to_reset
    return

def solution(n, k, cmd):
    answer=''
    linked_list = {} # 연결리스트
    stack = [] # 복구할 행
    dict_stack = {} # stack의 딕셔너리

    for i in range(n):
        dict_stack[i] = 0
        if i==0:
            linked_list[i] = [None, i+1]
        elif i==n-1:
            linked_list[i] = [i-1, None]
        else: linked_list[i] = [i-1, i+1]
    
    for i in cmd:
        method, num = '',''
        if len(i)>1:
            method, num = i.split()
        else: method = i

        if method=='U':
            for i in range(int(num)):
                tmp = linked_list[k][0]
                k = tmp
        elif method=='D':
            for i in range(int(num)):
                tmp = linked_list[k][1]
                k = tmp
        elif method=='C': k = clear_col(linked_list, stack, dict_stack, k)
        elif method=='Z': reset_col(linked_list, stack, dict_stack)

    for i in dict_stack:
        if dict_stack[i]:
            answer+='X'
        else: answer+='O'
    return answer


print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])) # OOOOXOOO
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])) #OOXOXOOO

'''
<연결리스트 문제>
1. 딕셔너리로 연결리스트 구현
2. U, D 메소드는 주어진 횟수에 맞게 연결리스트를 통해 이전, 다음 노드로 넘어간다.
3. C 메소드는 현재 행을 삭제하는데, 이때 Z메소드를 통한 복구를 위해 행의 정보는 건드리지 않고,
    이전노드의 다음노드와 다음노드의 이전노드 정보를 업데이트한다. 이후 복구를 위해 stack에 삭제한 행의 번호를 추가한다.
    조건1. 마지막 행을 삭제하는 경우: 이전노드의 마지막 노드값만을 None으로 변경한 후 k(현재 가리키는 행)를 현재 행의 이전노드로 변경한다.
    조건2. 첫행을 삭제하는 경우: 다음노드의 이전노드값을 None으로 변경한 후 k를 현재 행의 다음노드로 변경한다.
    조건3. 첫행과 마지막 행이 아닌 경우: 이전노드와 다음노드의 정보를 업데이트 한후 k를 현재 행의 다음노드로 변경한다.
4. Z 메소드는 최근에 삭제한 행을 복구하는데, 스택의 마지막 노드번호를 가져와 해당 노드와 연결된 노드들의 정보를 업데이트한다.
    조건1. 마지막행을 복구하는 경우: 이전노드의 다음노드를 복구할 노드로 연결한다.
    조건2. 첫행을 복구하는 경우: 다음노드의 이전노드를 복구할 노드로 연결한다.
    조건3. 첫행과 마지막행이 아닌 경우: 복구할 노드의 이전노드와 다음노드의 정보를 업데이트 한다.
    조건4. 복구 메소드 진행 시 k값은 변경을 하지 않는다.
5. 모든 작업이 완료된 후 dict_stack(삭제된 노드를 구별하는 딕셔너리)를 통해 각 노드의 정보를 읽어 경우에 따라 O,X 값을 추가한다.
'''