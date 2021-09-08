def solution(s):
    answer = ''
    s = s.split(' ')
    s = [int(n) for n in s]
    s = sorted(s)

    a_list = []
    a_list.append(str(s[0]))
    a_list.append(str(s[-1]))
    answer = ' '.join(a_list)
    return answer

solution('1 2 3 4')
solution('-1 -2 -3 -4')
solution('-1 -1')