def solution(s):
    answer=''
    s = list(s)
    s = sorted(s,reverse=True)
    answer += ''.join(s)
    return answer
solution('Zbcdefg')