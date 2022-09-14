def solution(s):
    answer = len(s)

    for i in range(len(s)//2, 0, -1):
        result = ''
        tmp = s[:i]
        cnt = 1

        for j in range(i, len(s) - i + 1, i):
            target = s[j:j+i]

            if tmp != target:
                if cnt > 1: result += f'{cnt}{tmp}'
                else: result += tmp
                tmp = target
                cnt = 1
            else: cnt += 1

        if cnt > 1: result += f'{cnt}{s[j:]}'
        else: result += s[j:]
        answer = min(answer, len(result))
    return answer

print(solution("aabbaccc")) # 7 => 2a2ba3c
print(solution("ababcdcdababcdcd")) # 9
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd")) # 17