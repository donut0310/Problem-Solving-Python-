def solution(n):
    answer = []
    flag=[i+1 for i in range(n)]
    f_sum=sum(flag)
    arr=[[0]*n for _ in range(n)]
    std_r,std_c=(0,n-1),(0,n-1) #가변적 범위
    start_r,start_c,cnt=0,0,1
    tmp=(0,0)
    if n==1:
        return [1]
    while std_r[0]!=std_r[1] and std_c[0]!=std_c[1]:
        if arr[start_r][start_c]!=0:
            print('go down')
            print('cnt:',cnt,'r,c:',start_r,start_c)
            print('tmp:',tmp)
            start_r, start_c = tmp[0]+1, tmp[1]
            print(std_r,std_c)
            print('new_r,new_c:',start_r,start_c)
            std_r=(std_r[0]+2,std_r[1]-1)
            std_c=(std_c[0]+1,std_c[1]-2)
            print(std_r,std_c)
            print('-----------')
        if arr[start_r][start_c]!=0: break
        if start_r!=std_r[1] and start_c==std_c[0]:
            tmp=(start_r,start_c)
            arr[start_r][start_c]=cnt
            start_r+=1
        elif start_r==std_r[1] and start_c!=std_c[1]:
            tmp=(start_r,start_c)
            arr[start_r][start_c]=cnt
            start_c+=1
        else:
            tmp=(start_r,start_c)
            arr[start_r][start_c]=cnt
            start_r-=1
            start_c-=1
        cnt+=1
        if cnt>f_sum:break
        print('next:',start_r,start_c,cnt)
    [print(i) for i in arr]
    print('-------------')
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                answer.append(arr[i][j])
    return answer
    
# print(solution(4))
# print(solution(5))
# print(solution(6))
print(solution(1))