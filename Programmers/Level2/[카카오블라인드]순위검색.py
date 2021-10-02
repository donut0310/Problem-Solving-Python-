import re
def search(subj,q):
    print(subj,'\n',q)
    answer =0 
    for i in subj:
        cnt=0
        for j,jv in enumerate(q):
            if jv=='-':
                cnt+=1
                continue
            elif j!=4:
                if jv!=i[j]:
                    break
                else:
                    cnt+=1 
            elif j==4 and jv<i[j]:
                cnt+=1
        if cnt==5:
            answer+=1
    return answer

def solution(info,query):
    answer,qarr,cpp,java,python = [],[],[],[],[]
    sumarr=[]

    [qarr.append(re.sub(r' and ',' ',i).split(' ')) for i in query]
    sumarr.extend(cpp)
    sumarr.extend(java)
    sumarr.extend(python)
    for i in info:
        subj = i.split(' ')
        if subj[0]=='cpp':
            cpp.append(subj)
        elif subj[0]=='java':
            java.append(subj)
        elif subj[0]=='python':
            python.append(subj)

    for q in qarr:
        subj = q[0]
        a=0
        if subj=='cpp':
            a=search(cpp,q)
        elif subj=='java':
            a=search(java,q)
        elif subj=='python':
            a=search(python,q)
        elif subj=='-':
            a=search(sumarr,q)
        answer.append(a)
    print(answer)
    return  answer

solution(["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"],
["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]
)