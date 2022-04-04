def solution(number,k):
    cnt,i=0,1
    stack=[number[0]]
    while cnt<k:
        if stack[-1] >= number[i]:
            stack.append(number[i])
            i+=1
            if len(stack)==len(number): # 스택이 같은 숫자로 뭉치고, number의 길이와 같아버린 경우 -> TC 5번 
                stack.pop()
                break
        else:
            stack.pop()
            cnt+=1
            if not len(stack): 
                stack.append(number[i])
                i+=1
    stack.extend(number[i:])
    return ''.join(stack)

print(solution('1924',2)) #'94'
print(solution('1231234',3)) #'3234'
print(solution('4177252841',4)) #'775841'
print(solution('921452',2)) #'9452'
print(solution('33',1))

'''
풀이
number의 첫번째 수를 스택에 담는다.
이후 number[i]번째 숫자부터 스택의 마지막 숫자와 비교한다
<조건>
1.스택의 마지막 숫자가 더 크거나 같은 경우 number[i]의 숫자를 추가해준다.
1-1. 이때 스택의 원소 개수가 number의 원소 개수와 같아지면 -> TC 5번
    스택의 마지막 원소를 삭제하고 cnt를 1 증가시켜준다.
2.스택의 마지막 숫자가 더 작은 경우엔 스택의 마지막 숫자를 삭제하고 cnt를 1 증가시켜준다.
2-1. 이때 스택이 비어버린 경우엔 현재 number[i]의 숫자를 스택에 다시 넣어준다.
3. cnt값이 k와 같아지는 경우 루프를 탈출하며 현재까지 스택에 담긴 숫자들을 문자열로 변환해 반환한다.
'''