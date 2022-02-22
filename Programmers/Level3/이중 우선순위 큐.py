def swap(heap,tmp,parent):
    heap[tmp],heap[parent]=heap[parent],heap[tmp]
    return heap

def max_heapify(heap,mid):
    size = len(heap)
    parent=mid
    left = parent*2
    right = parent*2+1
    tmp = parent
    
    if left<size and heap[left]>heap[tmp]:
        tmp=left
    if right<size and heap[right]>heap[tmp]:
        tmp=right
    if tmp!=parent:
        heap=swap(heap,tmp,parent)
        heap=max_heapify(heap,tmp)
    return heap

def min_heapify(heap,mid):
    size = len(heap)
    parent=mid
    left = parent*2
    right = parent*2+1
    tmp = parent
    if left<size and heap[left]<heap[tmp]:
        tmp=left
    if right<size and heap[right]<heap[tmp]:
        tmp=right
    if tmp!=parent:
        heap=swap(heap,tmp,parent)
        heap=min_heapify(heap,tmp)
    return heap

def build_max_heap(heap):
    mid = len(heap)//2
    for i in range(mid,0,-1):
        heap=max_heapify(heap,i)
    return heap

def build_min_heap(heap):
    mid = len(heap)//2
    for i in range(mid,0,-1):
        heap=min_heapify(heap,i)
    return heap

def solution(operations):
    heap = [0]

    for opt in operations:
        opt = opt.split(' ')
        if opt[0]=='I':
            heap.append(int(opt[1]))
        elif len(heap)>1 and opt[0]=='D' and opt[1]=='1':
            heap=build_max_heap(heap) #최대힙 구성
            heap[1]=heap[len(heap)-1] #최대값 루트 삭제
            heap.pop()
        elif len(heap)>1 and opt[0]=='D' and opt[1]=='-1':
            heap=build_min_heap(heap) #최소힙 구성
            heap[1]=heap[len(heap)-1] #최소값 루트 삭제
            heap.pop() 
    if len(heap)==1:return[0,0]
    heap=heap[1:]
    return [max(heap),min(heap)]

# print(solution(["I -45", "I 653", "D 1"])) # [333,-45]
# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333,-45]
# print(solution(["I 16","D 1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
# print(solution(["I 10","I 0","I -5"]))
# print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"])) #[6,5]
# print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"])) #[8,3]

# 큐가 비어있을 때 삭제 명령이 들어온 경우에 대해 예외처리를 하지 않아 리스트 인덱스 에러가 발생하였다.
# 최대힙 삭제인 경우와 최소힙 삭제인 경우에 대해서 위 예외처리를 적용한 후 정답
# heapify => 현재 배열 사이즈를 2로 나눈 값을 mid 변수로 포문을 역으로 수행한다.
# 각 mid 인 경우에 대해서 리프노드들과 비교 후 swap을 수행한다.
# swap이 이루어진 경우, 당시 리프노드의 인덱스를 기준으로 heapify를 재귀수행한다.

# 최대 or 최소 값 삭제
# 각 경우에 대해 최대힙 or 최소힙으로 구성한 후 루트노드와 말단 노드를 swap한 후 말단 노드로 이동한 루트노드를 pop
# 이후 경우에 따라서 최대힙 or 최소힙으로 heapify 를 진행
# 위 문제의 경우 경우에 따라 최대힙 or 최소힙으로 유동적으로 바뀌기 때문에 heapify를 진행하지 않고 
# 분기가 시작되면 먼저 heapify 를 진행한 후 루트노드와 말단노드에 대한 swap 및 말단노드 삭제 작업만 수행한다.