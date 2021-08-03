
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n==i*i:
            answer = (i+1)*(i+1)
            break
        elif n<i*i:
            answer = -1
            break
    return answer

solution(121)
solution(3)