import re
def solution(s):
    answer = []
    s_list = []
    st = []
    temp = ''
    for i in s[1:len(s)-1]:
        if i=='{':
            pass
        elif i==',':
            if len(temp)>0:
                st.append(int(temp))
                temp=''
            else:
                pass
        elif i=='}':
            if len(temp)>0:
                st.append(int(temp))
                s_list.append(st)
                st=[]
                temp=''
        elif re.match('[0-9]',i):
            temp += ''.join(i)
    s_list = sorted(s_list,key= lambda x:len(x))    
    for i in range(len(s_list)):
        target = s_list[i][0]
        for j in range(i+1,len(s_list)):
            index = s_list[j].index(target)
            s_list[j].pop(index)
        answer.append(target)
    return answer