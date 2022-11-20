def solution(begin, end):
    answer = []
    
    for num in range(begin, end + 1):
        flag = 0
        if num == 1: 
            answer.append(0)
            continue
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                d = num // i
                if d != num and d <= 10000000:
                    answer.append(d)
                    flag = 1
                    break
        if not flag: answer.append(1)
    return answer

print(solution(1, 10)) # [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]


'''
1부터 시작하는 answer 배열의 인덱스는 현재 숫자를 의미한다.
각 자리는 현재 인덱스를 넘지않는 현재 인덱스의 약수 중 최대값이 해당하게되는 규칙을 알 수 있다.
begin ~ end에 해당하는 숫자들을 위 조건에 맞는 수를 구해 배열에 삽입한다.
이때, 10000000번째 블록을 넘을 땐 1을 삽입하는 문제 조건을 만족하기 위해 if문으로 분기한다.
'''