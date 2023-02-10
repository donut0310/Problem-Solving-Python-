import math

def solution(x, y, n):
    answer, MAX = 0, math.inf
    dp = [0] * (y+1)
    
    for i in range(x+1, y+1):
        a, b, c = MAX, MAX, MAX
        if i-n >= x: a = dp[i-n]
        if i%2 == 0 and i//2 >= x: b = dp[i//2]
        if i%3 == 0 and i//3 >= x: c = dp[i//3]
        
        dp[i] = min(a, b, c) + 1

    answer = dp[y] if dp[y] < math.inf else -1
    return answer

'''
<조건>
세가지 연산이 가능
x - n
x * 2
x * 3

<풀이>
DP 이용
1. x ~ y 에 포함되는 숫자들을 문제 조건 3가지 연산으로 각각 계산한다.
2. 이때 계산의 결과가 x값보다 작은 경우엔 해당 숫자를 연산으로 만들 수 없기 때문에 무시한다.
3. 결과값이 x보다 크거나 같은 경우엔 연산이 가능한 숫자이며 dp[결과값]을 통해 이전 연산 결과(인덱스의 숫자가 만들어지기 까지의 최소 연산 횟수)를 구한다.
4. 3에서 구한 값 중 최소값(3가지 연산에 의한)에 +1 한 값이 현재 숫자를 만들기 위한 최소 연산 횟수가 보장된다.
'''