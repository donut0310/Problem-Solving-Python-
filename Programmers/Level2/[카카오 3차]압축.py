def solution(msg):
    answer=[]
    index = {}
    cnt=1
    for i in range(65,91):
        index[chr(i)] = cnt
        cnt+=1

    run=0
    while run<len(msg):
        target = ''
        if run is not len(msg)-1:
            for j in range(run+1,len(msg)+1):
                tmp = ''.join(msg[run:j])
                if tmp in list(index.keys()):
                    target = tmp
                    if j>=len(msg):
                        answer.append(index[target])
                        return answer
                else:
                    index[tmp]=cnt
                    cnt+=1
                    answer.append(index[target])
                    run=j-2
                    break
        else:
            answer.append(index[msg[run]])
        run+=1
    return answer

solution('KAKAO')
# solution('TOBEORNOTTOBEORTOBEORNOT')
solution('ABABABABABABABAB')