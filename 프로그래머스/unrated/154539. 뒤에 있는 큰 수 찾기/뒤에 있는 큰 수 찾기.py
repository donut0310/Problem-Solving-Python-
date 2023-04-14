def solution(numbers):
    answer = []
    stack = []
    
    start = len(numbers) - 1
    
    for i in range(start, -1, -1):
        num = numbers[i]
        
        if not stack:
            stack.append(num)
            answer.append(-1)
            continue
        
        while stack:
            tmp = stack[-1]
            
            if num < tmp:
                answer.append(tmp)
                break
            else: 
                stack.pop()
                if not stack: answer.append(-1)        
                
        stack.append(num)
        
    answer = answer[::-1]
    return answer