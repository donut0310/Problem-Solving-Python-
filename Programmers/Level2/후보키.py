from itertools import combinations, permutations

def solution(relation):
    answer=[]
    r=[]
    index = [i for i in range(len(relation[0]))]
    for i in index:
        r.extend(list(combinations(index,i+1)))

    for i in r:
        lis = []
        for j in relation:
            a = ''
            for k in i:
                a+=j[k]
            lis.append(a)
        if len(set(lis))==len(lis):
            answer.append(i)
    _a = answer[::]
    for i in range(len(answer)-1):
        for j in range(i+1,len(answer)):
            s = answer[i]+answer[j]
            if len(answer[j])==len(set(s)) and len(set(s))!=len(s):
                if answer[j] in _a:
                    _a.remove(answer[j])
    return len(_a)
solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
solution([["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]])
solution([["a","1","aaa","c","ng"],["a","1","bbb","e","g"],["c","1","aaa","d","ng"],["d","2","bbb","d","ng"]])