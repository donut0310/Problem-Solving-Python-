def solution(nums):
    answer = 0
    stack = []
    cnt = 0
    for n in nums:
        flag = 0 
        if cnt>=len(nums)/2:
            break
        for item in stack:
            if n==item:
                flag=1
                break   
        if flag==0:
            stack.append(n)
            cnt+=1
    answer = len(stack)
    return answer

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])