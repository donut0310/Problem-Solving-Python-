def solution(n, cores):
    answer = 0
    if n<=len(cores):
        return n
    n-=len(cores)
    left, right = 1, n*min(cores)

    #이분 탐색
    while left<right:
        mid = (left+right)//2 
        cnt=0
        for core in cores:
            cnt += mid//core
        if cnt>=n:
            right = mid
        else:
            left=mid+1
            
    for core in cores:
        n-=(right-1)//core
    for i in range(len(cores)):
        if right%cores[i]==0:
            n-=1
            if n==0:
                return i+1

print(solution(6,[1,2,3]))
