def separation(p):
    _u,u=[],[]
    
    for i in p:
        if len(u)==0:
            u.append(i)
            _u.append(i)
            continue
        if _u[-1]!=i:
            u.append(i)
            _u.pop()
        else:
            u.append(i)
            _u.append(i)
        if len(_u)==0:
            break
    return ''.join(u), p[len(u):]

def isUpright(str):
    tmp = []
    print(str)
    for i in range(len(str)):
        if len(tmp)==0:
            if str[i]==')': return False
            tmp.append(str[i])
            continue
        if tmp[-1]!=str[i]:
            tmp.pop()
        else: tmp.append(str[i])
    if len(tmp)==0: return True
    else: return False

def reverse(str):
    tmp = []
    for i in str:
        if i=='(': tmp.append(')')
        elif i==')': tmp.append('(')
    return tmp

def solution(p):
    if isUpright(p):
        return p
    # 1
    str = ''
    if len(p)==0: return ''
    # 2 w를 u,v로 분리
    u,v = separation(p)
    # 3 u가 '올바른 괄호  문자열'이면 1단계부터 다시
    if isUpright(u):
        u+=''.join(solution(v))
    else:
        str+='('
        str+=''.join(solution(v))
        str+=')'
        u=u[1:len(u)-1]
        str+=''.join(reverse(u))
        return str
    u+=''.join(str)
    return u


solution("(()())()")
# solution(")(")
# solution("()))((()")