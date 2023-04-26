import math

def recur(number, tree, size, index):
    if index > size: return

    parent =  len(number) // 2 # 부모 노드 인덱스
    tree[index] = number[parent]
        
    left = number[:parent] # 부모 노드 기준 왼쪽 노드들(다음 재귀함수에서 서브트리가 된다.)
    recur(left, tree, size, index * 2)
    
    right = number[parent+1:] # 부모 노드 기준 오른쪽 노드들(다음 재귀함수에서 서브트리가 된다.)
    recur(right, tree, size, index * 2 + 1)
    return

def is_tree_possible(tree):
    for i in range((len(tree)-1) // 2, 0, -1):
        if not tree[i] and (tree[i*2] or tree[i*2+1]): 
            return False
    return True
    
    
def solution(numbers):
    answer = []
    
    '''
    1. 주어진 수를 이진수로 바꾼 뒤 트리의 높이를 구해준다.
    2. 포화 이진 트리의 노드 수는 2**높이 -1개 이고, 이진수의 길이와 포화 이진 트리의 노드 수의 차이만큼 이진수 앞에 0을 붙여준다.
    3. 이진수 앞에 0을 몇개를 붙이든 이진수는 똑같은 수를 만족하게 된다.
    4. 0을 붙인 이진수(중위순회 결과)는 가운데 수가 루트가 되고, 루트 기준 왼쪽은 모두 왼쪽 자식, 오른쪽은 모두 오른쪽 자식을 만족한다.
    '''
    for number in numbers:
        number = bin(number)[2:]
        height = math.ceil(math.log2(len(number)+1))
        number = list(map(int, ('0' * (2**height - 1 - len(number)) + number)))

        # 루트노드 기준 재귀
        tree = [0] * (len(number) + 1)
        recur(number, tree, len(tree)-1, 1) # 분할될 서브트리, 원래 트리, 노드 개수, 시작 부모 노드
        
        if is_tree_possible(tree): answer.append(1)
        else: answer.append(0)
    
    return answer