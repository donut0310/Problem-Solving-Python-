def get_balanced_string(w):
    stack = []
    u, v = '', ''

    for i, s in enumerate(w):
        u += s
        if i == 0: stack.append(s)
        else:
            if stack[-1] == s: stack.append(s)
            else: stack.pop()
            
        if not stack: 
            v = w[i+1:]
            break

    return u, v

def is_correct_string(w):
    stack = []

    for i, s in enumerate(w):
        if not stack and s == ')': return False
        if i==0: stack.append(s)
        else:
            if stack and stack[-1] != s: stack.pop()
            else: stack.append(s)

    if not stack: return True
    else: return False

def reverse(w):
    tmp = ''
    for i in w:
        if i == '(': tmp += ')'
        else: tmp += '('
    return tmp

def recur(p): 
    if not p: return '' # 1
    u, v = get_balanced_string(p) # 2

    if is_correct_string(u): # 3
        u += recur(v)
        return u
    else: # 4
        tmp = '('
        tmp += recur(v)
        tmp += ')'
        u = u[1:-1]
        tmp += reverse(u)
        return tmp
        
def solution(p):
    if is_correct_string(p): return p

    answer = ''
    answer = recur(p)  
    return answer

# print(solution("(()())()")) # "(()())()"
# print(solution(")(")) # "()"
print(solution("()))((()")) # "()(())()"
