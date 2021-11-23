def solution(s):
    answer = len(s)
    tail=''
    for i in range(len(s)//2):
        new_str=''
        cnt=0
        std=s[:i+1]
        for j in range(0,len(s),i+1):
            comp = s[j:j+i+1]
            print(i,j,std,comp)
            if std==comp: cnt+=1
            else:
                if cnt>1:
                    new_str+=f'{cnt}'+std
                else: 
                    new_str+=std
                cnt=1
                std=comp
            if i==len(s)//2 and cnt==2:
                new_str+=f'{cnt}'+std
                if len(new_str)<=answer:
                    return len(new_str)
            if cnt>1:
                tail=f'{cnt}'+comp
            else: tail=comp
        new_str+=tail
        if len(new_str)<answer:
            answer=len(new_str)
    return answer

# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
print(solution("aaa"))