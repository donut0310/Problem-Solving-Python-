def binary(n):
    cnt = 0
    while n>0:
        if n%2!=0:
            cnt+=1
        n//=2
    return cnt

def solution(n):
    answer = 0
    binary_n = binary(n)
    while True:
        n+=1
        binary_num = binary(n)
        if binary_n == binary_num:
            answer=n
            break
    return answer

solution(78)
solution(15)