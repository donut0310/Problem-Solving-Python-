from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        tmp = prices.popleft()
        cnt = 0
        
        for p in prices:
            if tmp > p: 
                cnt += 1
                break
            else: cnt += 1
            
        answer.append(cnt)
    return answer