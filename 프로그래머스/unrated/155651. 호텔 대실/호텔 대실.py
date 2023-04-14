def time_converter(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    answer = 0
    dp = [0] * 1451
    
    for start, end in book_time:
        start, end = time_converter(start), time_converter(end)  
        dp[start] += 1
        dp[end+10] -= 1

    # 누적합
    for i in range(1, 1451):
        dp[i] += dp[i-1]
        
    answer = max(dp)
    return answer