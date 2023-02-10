def time_converter(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def solution(book_time):
    answer = 0
    arr = [0] * 1451
    
    for start, end in book_time:
        start, end = time_converter(start), time_converter(end)
        arr[start] += 1
        arr[end+10] -= 1
    
    # 구간합
    for i in range(1, 1001):
        arr[i] += arr[i-1]
        answer = max(answer, arr[i])

    return answer

'''
<풀이>
기본적인 구간합 풀이로 진행

<주의>
각 객실마다 대여 시간이 끝나고 10분간 청소 시간이 존재한다.
이때는 다음 손님이 사용 불가능하다.
따라서 기본 이용시간 start ~ end 보다 10분 더 사용중인 것으로 간주해야 한다.
'''