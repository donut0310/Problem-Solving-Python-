from itertools import permutations
import re
def calculate(a,b,operand):
    if operand == '-': return a-b
    elif operand == '+': return a+b
    elif operand == '*': return a*b

def solution(expression):
    answer = 0
    arr,start,exp=[],0,set()
    for i,s in enumerate(expression): # expression 분리
        if not re.match('[0-9]',expression[i]):
            arr.extend([int(expression[start:i]),expression[i]])
            exp.add(expression[i])
            start=i+1
    arr.append(int(expression[start:]))
    exp_perm = permutations(exp,len(exp)) # 연산자 조합 구하기
    for p in exp_perm: # 조합별 최대값 구하기
        tmp = arr[::] # copy
        for e in p:
            while e in tmp:
                index = tmp.index(e)
                if index==1: tmp = [calculate(tmp[index-1],tmp[index+1],e)]+tmp[index+2:]
                else: tmp = tmp[:index-1]+[calculate(tmp[index-1],tmp[index+1],e)]+tmp[index+2:]
        if abs(tmp[-1])>answer: answer = abs(tmp[-1])
    return answer

# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

# 풀이
# expressino을 숫자와 연산자로 분리해 arr배열에 저장한다.
# 추가로 연산자만 따로 exp(set집합)에 저장한다.
# exp의 조합을 구한다.
# arr배열의 복사본인 tmp를 만들어 각 조합별 연산자의 순서대로 수식을 계산한다.
# 이때, 하나의 수식이 여러개인 경우가 있기에 while문을 이용해 복수개의 같은 수식을 처리한다.
