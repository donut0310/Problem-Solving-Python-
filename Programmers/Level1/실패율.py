def cal(N,stages):
    obj={}
    for i in range(1,N+1):
        cnt = 0 
        failuer = 0
        for j in stages:
            if i<j:
                cnt+=1
            elif i==j:
                cnt+=1
                failuer+=1
        if failuer==0:
            obj[i]=0
        else: obj[i]=failuer/cnt
    obj = sorted(obj,key = lambda x:obj[x], reverse=True)
    return obj
def solution(N, stages):
    answer = cal(N,stages)
    return answer

solution(5,[2,1,2,6,2,4,3,3])
solution(5,[4,4,4,4,4])