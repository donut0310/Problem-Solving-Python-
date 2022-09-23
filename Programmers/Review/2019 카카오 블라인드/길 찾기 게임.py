import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node):
        self.root = Node(node[0], node[1], node[2])
    
    def insert(self, node):
        parent = self.root
        x = node[0]

        while True:
            if x < parent.x:
                if parent.left == None:
                    parent.left = Node(node[0], node[1], node[2])
                    break
                else: parent = parent.left
            elif x > parent.x:
                if parent.right == None:
                    parent.right = Node(node[0], node[1], node[2])
                    break
                else: parent = parent.right

    def preorder(self, node:Node, arr):
        if node == None: return
        arr.append(node.num)
        self.preorder(node.left, arr)
        self.preorder(node.right, arr)

    def postorder(self, node:Node, arr):
        if node == None: return
        self.postorder(node.left, arr)
        self.postorder(node.right, arr)
        arr.append(node.num)

def solution(nodeinfo):
    answer = [[]]

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    nodeinfo.sort(key=lambda x:-x[1])

    tree = Tree(nodeinfo[0])
    
    for node in nodeinfo[1:]:
        tree.insert(node)

    prelist, postlist = [], []
    tree.preorder(tree.root, prelist)
    tree.postorder(tree.root, postlist)

    answer.append(prelist)
    answer.append(postlist)

    return answer[1:]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

