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
    5. 4과정에서 중위 순회 결과 이진수를 원래 이진트리로 변형한다.
    6. 원래 이진트리에서 마지막 비단말 노드부터 루트노드로 거슬러 올라가면서 본인이 0일 때 자식노드 값 중 1이 있는 경우를 찾는다.
    7. 6과정에 만족하면 만들어질 수 없는 이진수이기 때문에 False를 반환하고, 만족하지 않는다면 만들 수 있는 이진수이기 때문에 True를 반환한다.
    8. 주의) 비단말 노드의 값이 0일 때, 자식노드들도 0인 경우는 만들 수 있는 이진수에 해당한다.
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