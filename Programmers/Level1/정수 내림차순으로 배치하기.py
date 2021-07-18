def solution(n):
    n = list(str(n))

    n = sorted(n,reverse=True)
    answer=''
    for i in n:
        answer+=i
    return int(answer)

solution(118372)