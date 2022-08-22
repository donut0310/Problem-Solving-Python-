from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_1 = sum(queue1)
    target = (sum_1 + sum(queue2)) // 2

    while queue1 and queue2:
        if sum_1 == target: return answer
        if sum_1 > target:
            sum_1 -= queue1.popleft()
        elif target > sum_1:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum_1 += tmp

        answer += 1

    return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2],[1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5])) # -1

'''
<풀이>
1. 두 큐의 합이 같기 위해선 한 큐의 값이 target(두 큐의 합의 절반)과 같은지 확인하면 된다.
2. 시간초과를 해결하기 위해 sum 함수는 반복문 내에서 사용하지 않고, sum_1 변수(int)를 누적합을 이용하여 계산한다.
3. queue1을 기준으로 sum_1 변수와 target변수의 대소차이에 따라 큐를 갱신한다.

<참고>
큐를 하나로 기준잡지 않고, 두 개의 큐를 모두 타겟과 비교하며 서로 큐에서 빼고 넣고를 반복하다보면 시간초과가 발생한다.
하나의 큐를 기준으로 target 값과 대소비교를 하면 더 빨리 답에 접근이 가능하다.
'''