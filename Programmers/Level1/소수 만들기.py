def isOdd(v_sum):
    cnt=0
    i = 1
    while(i<=v_sum):
        if v_sum%i == 0:
            cnt+=1
        if cnt>2:
            break
        i+=1
    if cnt>2: return 0
    return 1

def solution(nums):
    nums_len = len(nums)
    cnt = 0
    v_sum = 0
    i = 0
    j=i+1
    k=j+1
    while(k<nums_len):
        v_sum=nums[i]+nums[j]+nums[k]
        cnt += isOdd(v_sum)
        if j==nums_len-2 and k==nums_len-1:
            i+=1
            j=i+1
            k=j+1
        elif k==nums_len-1:
            j+=1
            k=j+1
        else:
            k+=1
    return cnt