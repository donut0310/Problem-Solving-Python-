from itertools import combinations

def solution(relation):
    arr = []
    unique_keys = []
    [print(i) for i in relation]
    for i in range(1, len(relation[0])+1):
        arr.extend(combinations(range(len(relation[0])), i))

    # 유일성 만족 경우 추출
    for comb in arr:
        tmp_arr = []
        for item in relation:
            tmp = ''
            for index in comb:
                tmp += item[index]
            tmp_arr.append(tmp)

        if len(tmp_arr) == len(set(tmp_arr)): unique_keys.append(comb)

    # 최소성 만족 경우 추출
    _copy = unique_keys[::]
    for i in range(len(unique_keys)-1):
        for j in range(i+1, len(unique_keys)):
            tmp = unique_keys[i] + unique_keys[j]
            set_tmp = set(tmp)
            if len(tmp) != len(set_tmp):
                if tuple(set_tmp) in _copy: _copy.remove(tuple(set_tmp))
                
    return len(_copy)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	))
# 2

print(solution([["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]))
# 3