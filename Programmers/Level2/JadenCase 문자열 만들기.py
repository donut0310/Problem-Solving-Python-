import re

def solution(s):
    answer = ''
    s = s.lower()
    s = list(s)
    regex = re.compile('[0-9]+')

    for i in range(len(s)):
        if i==0 and not regex.match(s[i]):
            s[i] = s[i].upper()
        elif s[i-1]==' ' and not regex.match(s[i]):
            s[i] = s[i].upper()
        else:
            pass
    answer = ''.join(s)
    return answer

solution('3people   unFollowed    me')
solution('for the   last week')