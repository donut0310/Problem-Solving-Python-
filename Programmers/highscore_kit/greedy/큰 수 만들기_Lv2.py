# def solution(number, k):
#     answer = ''

#     start = (0, '0')
#     while k > 0:
#         tmp = start[0] # for loop의 범위를 실질적으로 인덱스 0 ~ 0 + a로 하기 위한 변수

#         for i in range(start[0], start[0] + k + 1):
#             n = number[i]
#             if n > start[1]: start = (i, n)
        
#         answer += start[1]
#         k -= start[0] - tmp # 인덱스 변경
#         start = (start[0] + 1, '0')
#         tmp = start[0] 

#     answer += number[start[0]:]
#     return answer
'''
시간초과 1개, 런타임 1개
'''

def solution(number, k):
    cnt, i = 0, 1
    stack = [number[0]]
    answer = ''
    end = len(number)

    if len(set(list(number))) == 1: return number[:k]

    while cnt < k:
        n = number[i]
        if n <= stack[-1]:
            stack.append(n)
            i += 1
            if i == end: # TC 5
                stack.pop()
                break
        else:
            stack.pop()
            cnt += 1
            if not stack:
                stack.append(n)
                i += 1
        
    answer = ''.join(stack) + number[i:]
    return answer
print(solution("1231234", 3)) # '3234'
print(solution("4177252841", 4)) # '775841'
print(solution('921452',2)) #'9452'
print(solution('33',1)) # '3'
print(solution('654321', 1)) # '65432'
