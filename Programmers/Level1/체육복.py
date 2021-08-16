def solution(n, lost, reserve):
    answer = 0
    arr = [1]*n
    for i in reserve:
        arr[i-1]+=1
    for i in lost:
        arr[i-1]-=1
    for i in range(len(arr)):
        if i==0 and arr[i]==0:
            if arr[i+1]==2:
                arr[i+1]-=1
                arr[i]+=1
                continue
        elif i==len(arr)-1 and arr[i]==0:
            if arr[i-1]==2:
                arr[i-1]-=1
                arr[i]+=1
                continue
        elif arr[i]==0:
            if arr[i-1]==2:
                arr[i-1]-=1
                arr[i]+=1
            elif arr[i+1]==2:
                arr[i+1]-=1
                arr[i]+=1
    for i in arr:
        if i!=0:
            answer+=1
    return answer

solution(3,[1],[3])
# 2 0 0 0 2 2
# 0 2 2 0 0 2