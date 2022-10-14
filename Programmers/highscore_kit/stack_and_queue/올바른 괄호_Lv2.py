def solution(s):
    answer = True
    stack = []
    for i in s:
        if not stack:
            if i == ')': return False
            else: stack.append(i)
        else:
            if stack[-1] != i: stack.pop()
            else: stack.append(i)

    if len(stack): return False
    else: return True

print(solution("()()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False