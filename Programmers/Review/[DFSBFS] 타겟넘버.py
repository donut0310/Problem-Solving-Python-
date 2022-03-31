from collections import deque

def solution(numbers, target):
    q1,q2 = deque([numbers[0]]),deque([-numbers[0]])

    for i in numbers[1:]:
        tmp1,tmp2=[],[]
        while q1:
            e1 = q1.pop()
            e2 = q2.pop()
            tmp1.extend([e1+i,e1-i])
            tmp2.extend([e2+i,e2-i])
        q1,q2=tmp1,tmp2
        print(q1,q2)
    return q1.count(target) + q2.count(target)

print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))

# 순서가 변하지 않기 때문에 numbers의 시작 숫자를 양수 음수로 나눈 각각의 데크를 선언한다(q1,q2)
# numbers의 두번째 인덱스를 시작으로 q1,q1는 같은 길이를 보장하기에 q1을 기준으로 while문을 돌린다.
# 큐가 빌 때까지 각 큐의 원소에서 현재 numbers에 위치한 숫자를 더한 수와 뺀 수를 tmp 배열에 삽입 후 
# 큐가 비면 각 큐에 tmp 배열을 할당해준다.
# 모든 작업이 완료 된후 각각의 큐에서 target 숫자를 찾아 더한 후 반환한다.