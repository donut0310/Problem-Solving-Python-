def solution(n):
    answer = ''
    for i in range(1,n+1):
        if i % 2 ==0:
            answer+=''.join('박')
        else:
            answer+=''.join('수')
    return answer

solution(3)
solution(4)