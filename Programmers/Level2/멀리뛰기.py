def solution(n):
    arr = [1 for _ in range(n+1)]
    
    for i in range(2, n+1):
        arr[i] = arr[i-2] + arr[i-1]

    return arr[-1] % 1234567

'''
조건: 뛸 수 있는 칸은 1칸, 2칸

<풀이>

n이 1 일 때, 뛰는 방법의 수는 1
n이 2 일 때, 뛰는 방법의 수는 2
n이 3 일 때, 뛰는 방법의 수는 3
n이 4 일 때, 뛰는 방법의 수는 5
            .
            .
            .
n일 때, 뛰는 방법의 수는 n-2의 뛰는 방법의 수 + n-1의 뛰는 방법의 수
            
위의 규칙을 통해 피보나치 수열대로 진행함을 알 수 있다.

'''

print(solution(4)) # 5
print(solution(3)) # 3
