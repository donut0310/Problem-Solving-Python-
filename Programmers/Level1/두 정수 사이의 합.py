def solution(a, b):
    answer = 0
    if a==b:
        return a
    if a>b:
        temp=a
        a=b
        b=temp
    for i in range(a,b+1):
        answer+=i
    return answer

solution(3,5)
solution(3,3)
solution(5,3)
