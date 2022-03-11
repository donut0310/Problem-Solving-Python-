def solution(s):
    answer=len(s)
    test=''
    for i in range(len(s)//2):
        std = s[:i+1]
        cnt=0
        new_str=''
        for j in range(0,len(s),i+1):
            comp=s[j:j+i+1]
            if std==comp:cnt+=1
            else:
                if cnt>1: new_str+=f'{cnt}{std}'
                else: new_str+=std
                std=comp
                cnt=1
        if cnt>1: new_str+=f'{cnt}{std}'
        else: new_str+=std
        answer = len(new_str) if (len(new_str))<answer else answer
    return answer

# print(solution("aabbaccc")) #7
# print(solution("ababcdcdababcdcd")) #9
# print(solution("abcabcdede")) #8
# print(solution("abcabcabcabcdededededede")) #14
# print(solution("xababcdcdababcdcd")) #17

# 문자열을 1자, 2자, 3자 ~ 문자열의 절반길이까지만 조사를 하면 되기 때문에
# 첫번재 반복문의 범위를 주어진 문자열 s의 절반길이인 len(s)//2 로 지정한다.
# 반복문의 인덱스로 자른 문자를 std 변수에 저장한 뒤 std 변수의 길이만큼 문자열을 건너뛰며
# std 변수가 반복되는지 조사한다.
# 반복되면 반복되는 개수를 cnt에 증가 시키고 반복되지 않는 경우를 만났을때 cnt개수만큼
# 2*std를 만들어 새로운 문자열 new_str에 추가시킨다. 
# 만들어진 new_str변수의 길이가 처음 주어진 문자열 s의 길이보다 작은 경우 answer값에 
# new_str변수의 값을 갱신해준다.