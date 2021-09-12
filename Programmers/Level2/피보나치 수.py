# 재귀 => 타임아웃+런타임
# def recurse(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return recurse(n-1)+recurse(n-2)

# def solution(n):
    # answer = recurse(n)
    # print(answer)
    # return answer%1234567

# DP => Accept!
def solution(n):
    answer = [0,1]
    while len(answer)<=n:
        index = len(answer)
        answer.append(answer[index-1]+answer[index-2])    
    return answer[n]%1234567

solution(3)
solution(5)
solution(12)