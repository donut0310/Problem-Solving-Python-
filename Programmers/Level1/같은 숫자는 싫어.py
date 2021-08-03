def solution(arr):
    answer=[]
    i,j=0,0
    while i<len(arr):
        j=i
        while j<len(arr)-1 and arr[j] == arr[j+1]:
            j+=1
        answer.append(arr[i])
        i=j+1
    return answer

solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])