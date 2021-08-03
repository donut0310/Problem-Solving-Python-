def solution(x, n):
    answer = []

    for i in range(1,n+1):
        answer.append(x*i)
    return answer

solution(2,5)
solution(4,3)
solution(-4,2)