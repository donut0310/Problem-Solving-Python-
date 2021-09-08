def solution(A,B):
    answer = 0

    A = sorted(A,reverse=True)
    B = sorted(B)

    for i in range(len(A)):
        answer += (A.pop() * B.pop())
    return answer

solution([1,4,2],[5,4,4])
solution([1,2],[3,4])