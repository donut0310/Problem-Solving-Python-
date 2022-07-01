from collections import deque

def doZip(arr,lu,rb): # 변경된 or 변경되지 않은 arr, 압축 가능 여부 리턴
    std = arr[lu[0]][lu[1]]
    for i in range(lu[0],rb[0]+1):
        for j in range(lu[1],rb[1]+1):
            if arr[i][j]!=std: 
                return arr,False
    for i in range(lu[0],rb[0]+1):
        for j in range(lu[1],rb[1]+1):
            if i==lu[0] and j==lu[1]: continue
            arr[i][j]=-1
    return arr, True

def doSeperate(lu,rb): # 분할 된 영역들의 [(좌상단 좌표 ,우하단 좌표)] 리턴
    size = (rb[0]-lu[0]+1)//2

    s1 = ((lu[0],lu[1]),(lu[0]+size-1,lu[1]+size-1))
    s2 = ((lu[0],lu[1]+size),(lu[0]+size-1,lu[1]+size+size-1))
    s3 = ((lu[0]+size,lu[1]),(lu[0]+size+size-1,lu[1]+size-1))
    s4 = ((lu[0]+size,lu[1]+size),(lu[0]+size+size-1,lu[1]+size+size-1))
    return [s1,s2,s3,s4]

def solution(arr):
    answer = []
    queue = deque([((0,0),(len(arr)-1,len(arr)-1))]) # 좌상단 좌표, 우하단 좌표
    while queue:
        lu,rb = queue.pop()
        arr,isPossibleToZip = doZip(arr,lu,rb) # 쿼드 압축 가능 확인, 가능하다면 arr은 변경된 채 리턴, 가능 여부 리턴
        if not isPossibleToZip: # 압축이 되지 않은 경우 분할 가능 여부 확인
            if rb[0]-lu[0]==1: continue # 분할 불가
            else: queue.extend(doSeperate(lu,rb))

    x,y=0,0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]==0: x+=1
            elif arr[i][j]==1: y+=1
    answer = [x,y]
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4,9]
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]] )) 
# [10,15]

'''
<풀이>
1. 쿼드 압축 가능 확인 (분할 영역 내의 모든 수 확인)
1-1. 압축이 된다면 각 영역의 좌상단 좌표를 제외한 나머지 영역은 -1로 변경
2-2. 압축이 되지 않는다면, 분할이 가능한지 확인
2-3. 분할이 된다면 각 분할된 영역의 좌상단 좌표와 우하단 좌표를 큐에 삽입
3. 한 영역씩 큐에서 뽑아 1~2의 과정을 반복
4. 모든 압축이 끝난 후 arr 배열 내의  0과 1 카운트
'''
