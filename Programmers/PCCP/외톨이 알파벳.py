from collections import defaultdict
def solution(input_string):
    answer = ''
    info = defaultdict(tuple)
    
    for i, c in enumerate(input_string):
        if not info[c]:
            info[c] = (i, 0) #(마지막 인덱스, 후보 여부)
        else:
            if i - info[c][0] == 1:
                info[c] = (i, 0)
            else: 
                info[c] = (info[c][0], 1)
    
    arr = []
    for key in info:
        if info[key][1] == 1: arr.append(key)
    
    if len(arr) == len(input_string) or not arr: answer = 'N'
    else: answer = ''.join(sorted(arr))
    return answer