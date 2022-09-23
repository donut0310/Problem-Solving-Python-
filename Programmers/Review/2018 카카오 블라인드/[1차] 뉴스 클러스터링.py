from collections import defaultdict
import math
import re

def split_string(arr):
    result = defaultdict(int)
    for i in range(len(arr)-1):
        if len(re.sub('[^a-z]', '', arr[i:i+2])) == 2:
            result[arr[i:i+2]] += 1
    return result

def solution(str1, str2):
    answer = 0

    dict1 = split_string(str1.lower())
    dict2 = split_string(str2.lower())

    tmp1 = set(dict1.keys()) & set(dict2.keys())
    tmp2 = set(dict1.keys()) | set(dict2.keys())

    result1, result2 = 0, 0
    for i in tmp1:
        result1 += min(dict1[i], dict2[i])
    
    for i in tmp2:
        result2 += max(dict1[i], dict2[i])

    if result2 == 0: return 65536
    answer = math.floor(result1 / result2 * 65536)    

    return answer

print(solution("FRANCE", "french")) # 16384
print(solution("handshake", "shake hands")) # 65536
print(solution("aa1+aa2", "AAAA12")) # 43690
print(solution("E=M*C^2", "e=m*c^2")) # 65536

