def solution(n):
    arr =[0 for _ in range(n+1)]
    arr[0],arr[1] = 1,1

    for i in range(n-1):
        arr[i+2] = (arr[i]+arr[i+1])%1000000007   
    return arr[n]

print(solution(4)) # 5

'''
<풀이>
n의 크기마다 배치할 수 있는 타일의 모양은
n=1: 1
n=2: 2
n=3: 3
n=4: 5
n=5: 8
...
으로 피보나치 수열임을 확인할 수 있다.
'''