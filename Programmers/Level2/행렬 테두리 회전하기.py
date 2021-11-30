from collections import deque
def solution(rows, columns, queries):
    answer = []
    arr=[]
    cnt=1
    for i in range(rows):
        brr=[]
        for j in range(columns):
            brr.append(cnt)
            cnt+=1
        arr.append(brr)

    for i in queries:
        tmp=[]
        r,c=i[0]-1,i[1]-1
        queue=deque([arr[r+1][c]]) #시작 인덱스 아랫줄 값
        while r!=i[0] or c!=i[1]-1:
            queue.append(arr[r][c])
            arr[r][c]=queue.popleft()
            tmp.append(arr[r][c])
            if r==i[0]-1 and c!=i[3]-1:
                c+=1
            elif r!=i[2]-1 and c==i[3]-1:
                r+=1
            elif r==i[2]-1 and c!=i[1]-1:
                c-=1
            elif r!=i[0]-1 and c==i[1]-1:
                r-=1
        arr[r][c]=queue.popleft()
        tmp.append(arr[r][c])
        answer.append(min(tmp))
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))
# print(solution(6,6,[[2,2,5,4],[3,3,6,6]]))
# print(solution(6,6,[[2,2,5,4]]))