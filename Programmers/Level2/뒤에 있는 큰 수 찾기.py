def solution(numbers):
    answer = []
    stack = []
    
    for i in range(len(numbers)-1, -1, -1):
        if not stack: 
            answer.append(-1)
            stack.append(numbers[i])
            continue
            
        flag = 0
        while stack:
            tmp = stack[-1]
            if numbers[i] >= tmp:
                stack.pop()
            else:
                answer.append(tmp)
                flag = 1
                break
                
        if not flag: answer.append(-1)
        stack.append(numbers[i])
            
    return answer[::-1]

'''
조건: 자신보다 뒤에 있는 수 중에서 가장 크고 가까운 수를 찾아야 한다.

스택을 이용하여 리스트의 맨 뒤 순서부터 역순으로 위 조건에 해당하는 수를 찾는다.

자신보다 작거나 같은 수인 경우 스택에서 삭제를 반복한다.

자신보다 '큰 수'인 경우 해당하는 수는 스택을 이용했기 때문에 
'가장 가까운 수'라는 조건이 만족한다.

따라서 위 경우에는 answer 리스트에 해당하는 수를 삽입해준뒤 while문을 종료한다.
'''

