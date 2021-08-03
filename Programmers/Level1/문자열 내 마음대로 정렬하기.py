def solution(strings, n):
    answer = []
    for index in range(len(strings)):
        target = strings[index][n]
        strings[index]=(strings[index],target)
    
    strings.sort( key = lambda x:(x[1],x[0]))
    for index in strings:
        answer.append(index[0])
    return answer

solution(["sun", "bed", "car"],1)
solution(["abce", "abcd", "cdx"],2)