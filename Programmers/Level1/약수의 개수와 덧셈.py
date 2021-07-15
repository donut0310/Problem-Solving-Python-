def divisor(num):
    cnt = 0
    i=1
    while(i<=num):
        if num%i==0:
            cnt+=1
        i+=1

    if cnt%2==0: return num
    return -1*num

def solution(left,right):
    v_sum = 0
    for i in range(left,right+1):
        v_sum += divisor(i)
    return v_sum