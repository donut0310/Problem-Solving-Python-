import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.left, self.right = None, None

class Tree:
    def __init__(self, root):        
        self.root = Node(root[0], root[1], root[2])
        
    def insert(self, node):
        x = node[0]
        parent = self.root
        # recursive
        while True:
            if x > parent.x: # 부모 노드보다 x값이 큰 경우, 오른쪽 자식 노드가 됨
                if parent.right == None: # 부모 노드의 오른쪽 자식 노드가 존재하지 않은 경우, 현재 노드가 오른쪽 자식 노드가 됨
                    parent.right = Node(node[0], node[1], node[2])
                    break
                else: parent = parent.right
            if x < parent.x: # 부모 노드보다 x값이 작은 경우, 왼쪽 자식 노드가 됨
                if parent.left == None:
                    parent.left = Node(node[0], node[1], node[2])
                    break
                else: parent = parent.left
    
def preorder(parent, arr):
    if parent == None: return
    arr.append(parent.num)
    preorder(parent.left, arr)
    preorder(parent.right, arr)
        
def postorder(parent, arr):
    if parent == None: return
    postorder(parent.left, arr)
    postorder(parent.right, arr)
    arr.append(parent.num)
    

def solution(nodeinfo):
    answer = []
    # 노드 번호 추가
    for i in range(len(nodeinfo)):
        nodeinfo[i] = nodeinfo[i] + [i+1]

    nodeinfo.sort(key = lambda x:-x[1])   
    tree = Tree(nodeinfo[0])
    for i in nodeinfo[1:]:
        tree.insert(i)

    pre, post = [], []
    preorder(tree.root, pre)
    postorder(tree.root, post)
    answer.append(pre)
    answer.append(post)

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

'''
<풀이>
1. x좌표, y좌표, 노드 번호를 정보로 가지는 Node 클래스 구현
2. Node 객체를 정보로 가지는 Tree 클래스 구현
3. y축을 기준으로 nodeinfo 배열을 내림차순 정렬 한 뒤, 첫번째 원소(y축 값이 가장 큰 노드)를 tree의 루트노드로 초기화한다.
4. nodeinfo 배열에서 루트노드를 제외한 나머지 노드들을 트리에 삽입한다.
4-1. 트리에 삽입할 때, 선택된 노드(node)가 부모 노드(parent)의 x값과 대소비교를 한 뒤 삽입한다.
4-2. 만약 삽입해야할 위치에 다른 노드가 있다면, 해당 노드를 부모 노드로 변경하고 4-1 과정을 반복한다.
5. 트리에 모든 노드가 조건에 맞게 삽입이 되었다면, 전위 순회와 후위 순회한 결과를 answer에 삽입한 뒤 반환한다.
'''

