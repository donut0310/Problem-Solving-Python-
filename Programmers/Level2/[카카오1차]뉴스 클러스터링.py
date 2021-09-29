import re

def findAndSet(p1,p2):
    and_set=[]
    tmp1,tmp2=p1[:],p2[:]
    for i in tmp1:
        if i in tmp2:
            and_set.append(i)
            del tmp2[tmp2.index(i)]
    return and_set

def findSumSet(p1,p2,and_set):
    sum_set=[]
    sum_set.extend(p1)
    sum_set.extend(p2)
    for i in and_set:
        if i in sum_set:
            del sum_set[sum_set.index(i)]
    return sum_set

def strCheck(p):
    arr = []
    for i in p:
        s = re.match('^[a-zA-Z]*$',i)
        if s is not None:
            arr.append(s.group())
    return arr

def solution(str1, str2):
    # 조합
    p1,p2=[],[]
    p_str1,p_str2=[],[]
    [p1.append((str1[i:i+2]).lower())  for i in range(0,len(str1)-1)]
    [p2.append((str2[i:i+2]).lower()) for i in range(0,len(str2)-1)]

    # 알파벳 제외 문자 제거
    p_str1 = strCheck(p1)
    p_str2 = strCheck(p2)

    # 교집합
    and_set=[]
    if len(p_str1)<=len(p_str2):
        and_set=findAndSet(p_str1,p_str2)
    else:
        and_set=findAndSet(p_str2,p_str1)

    # 합집합
    sum_set = findSumSet(p_str1,p_str2,and_set)

    # 자카드 유사도
    if len(and_set)==0 and len(sum_set)==0:
        return 65536
    simillarity = int(len(and_set)/len(sum_set)*65536)
    return simillarity

solution('FRANCE','french')
solution('handshake','shake hands')
solution('aa1+aa2','AAAA12')
solution('E=M*C^2','e=m*c^2')