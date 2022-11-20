def solution(n, k):
    answer = []
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = i * dp[i-1]

    answer = [i for i in range(1, n+1)]
    result = []
    while n > 0:
        index = (k-1) // dp[n-1]
        result.append(answer[index])
        del answer[index]
        k %= dp[n-1]
        n -= 1 
        
    return result

print(solution(3, 5)) # [3, 1, 2]
print(solution(3, 6)) # [3, 1, 2]

'''
<풀이>
1. 1~n까지의 팩토리얼 계산 -> dp
2. 정답을 담을 배열 result와 1~n까지의 값을 담을 answer배열 초기화
3. k번째 숫자 조합을 찾기전에 규칙이 존재한다.
4. 전체 숫자 조합의 개수는 n!이다.
5. 각 숫자의 앞자리가 바뀌는 조건은 k // (n-1)! 이다.
6-1. 이때, 전체 숫자의 조합은 1부터 시작하기 때문에 배열의 인덱스 조정이 필요하다
6-2. 5에서의 공식을 다음과 같이 변경한다 -> (k-1) // (n-1)!
7. 6에서 얻은 값이 숫자조합의 첫번째 숫자를 가리킬 인덱스가 되고, 초기화한 answer배열에서의 인덱스에 해당하는 값을 result에 추가한다.
8. 다음으로 구해야할 자리수는 n-1개가 되기 때문에 n -= 1 연산을 진행하고 위 작업을 n > 0 인 동안 반복한다.
'''