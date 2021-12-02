def check(s):
    dict = {
        '(':'-',
        '[':'-',
        '{':'-',
        ')':'(',
        ']':'[',
        '}':'{'
    }
    stack=[]
    for i in range(len(s)):
        if len(stack)==0: stack.append(s[i])
        elif dict[s[i]]==stack[-1]: 
            stack.pop()
        else: stack.append(s[i])
    if len(stack)==0: return True
    else: return False

def solution(s):
    answer = 0

    for i in range(len(s)):
        tmp=s[i:]+s[:i]
        if check(tmp): answer+=1
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))