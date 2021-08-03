def solution(n):
    arr = [True] * n
    m = int(n**0.5)
    for i in range(2,m+1):
        if arr[i-1]==True:
            for j in range(i+i,n+1,i):
                arr[j-1]=False
    return (arr.count(True)-1)
solution(10)
solution(5)