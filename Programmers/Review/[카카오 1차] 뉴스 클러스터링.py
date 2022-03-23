import re
from collections import defaultdict

def make_multiple_set(s):
    tmp=defaultdict(int)
    for i in range(len(s)-1):
        word = ''.join(s[i:i+2].lower())
        if re.match('^[a-z]*$',word):
            tmp[word]+=1
    return tmp

def solution(str1, str2):
    answer = 0

    # 다중집합 만들기
    s1 = make_multiple_set(str1)
    s2 = make_multiple_set(str2)
    if not len(s1) and not len(s2): return 65536

    # 교집합
    and_set=[]
    for i in s1:
        if i in s2:
            cnt=min(s1[i],s2[i])
            and_set+=[i]*cnt
    # 합집합
    s1_set,s2_set = [],[]
    [s1_set.extend([i]*s1[i]) for i in s1]
    [s2_set.extend([i]*s2[i]) for i in s2]
    sum_set = s1_set+s2_set
    for i in and_set:
        del sum_set[sum_set.index(i)]
    answer = int(len(and_set)/len(sum_set)*65536)
    return answer

print(solution('FRANCE','french')) #16384
print(solution('handshake','shake hands	')) #65536
print(solution('aa1+aa2	','AAAA12')) #43690
print(solution('E=M*C^2	','e=m*c^2	')) #65536

# 입력으로 주어진 문자열을 2자 단위로 잘라 다중집합을 만든다.
# 이때 알파멧 영문자만 가능하도록 정규식을 구하고, 대소문자 구별을 하지 않기 위해 모두 소문자로 바꿔준다.
# 문제 조건에 맞게 교집합과 합집합을 구한뒤 자카드 유사도 공식을 사용한다.