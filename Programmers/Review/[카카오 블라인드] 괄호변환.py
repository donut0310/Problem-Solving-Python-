def seperation(p): #문자열 p를 균형잡힌 괄호 문자열 u,v로 분리
    u,_u=[p[0]],[p[0]]
    for i in range(1,len(p)):
        if p[i]!=_u[-1]: _u.pop()
        else: _u.append(p[i])
        u.append(p[i])
        if not len(_u):
            break
    return ''.join(u), p[len(u):]

def is_right(u): #올바른 문자열 검사
    if u[0]==')': return False
    tmp=[u[0]]
    for i in range(1,len(u)):
        if tmp[-1] != u[i]: tmp.pop()
        else: tmp.append(u[i])
    if len(tmp): return False
    return True

def solution(p):
    str=''
    if not len(p): return '' #1
    u,v=seperation(p) #2
    if is_right(u): u+=solution(v) #3
    else: #4
        str+='(' #4-1
        str+=solution(v) #4-2
        str+=')' #4-3
        u=u[1:-1] #4-4
        tmp=''
        for i in range(len(u)):
            if u[i]=='(': tmp+=')'
            else: tmp+='('
        str+=tmp
        return str
    u+=str
    return u
    
print(solution("(()())()"))
print(solution(')('))
print(solution("()))((()"))

#solution 함수는 문제에 주어진 로직을 따라간다
#seperation 함수는 주어진 문자열을 균형잡힌 문자열(괄호의 개수가 서로 같은 경우)로 나누어 반환하는 함수다
#주어진 변수 p를 기준으로 u,_u변수는 p의 값을 하나씩 넣어주는데, _u변수는 서로 반대되는 괄호인 경우 append가 아닌 pop을 통해 상쇄한다.
#_u변수가 []이 되는 순간 u변수는 균형잡힌 문자열이 되며 p변수를 u변수로 자르고 난 뒤의 값 또한 균형잡힌 문자열이된다.
# 이후 is_right변수를 통해 올바른 문자열인지 검사한 후 문제에 주어진 로직을 따라간다.