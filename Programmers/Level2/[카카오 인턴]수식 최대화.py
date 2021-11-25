import re
from itertools import permutations

def cal(a,e,b):
    if e=='-':return a-b
    elif e=='+':return a+b
    elif e=='*': return a*b

def solution(expression):
    org,exp=[],[]
    s=''
    for i in range(len(expression)):
        if re.match('^[0-9]',expression[i]):
            s+=expression[i]
        else:
            org.extend([int(s),expression[i]])
            exp.append(expression[i])
            s=''
    org.append(int(s))
    p = list(permutations(set(exp),len(set(exp))))

    max_n=0
    print(org)
    print('----------')
    for i in p:
        tmp=org[::]
        print(i)
        for j in i:
            index=1
            while index<len(tmp)-1:
                if tmp[index]==j:
                    n=cal(tmp[index-1],j,tmp[index+1])
                    tmp[index-1]=n
                    print(j,n,index)
                    print('before:',tmp)
                    if index+2>=len(tmp):
                        tmp=tmp[:index]
                    else:
                        tmp=tmp[:index]+tmp[index+2:]
                        index-=2
                    print('after:',tmp)
                index+=2
        if abs(tmp[0])>max_n: max_n=abs(tmp[0])
        print("max:",max_n)
        print('--------------')
    return max_n

# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))
print(solution("1+1-2"))