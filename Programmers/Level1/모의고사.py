def score(a,b,c,answer,result):
    a_len = len(a)
    b_len = len(b)
    c_len = len(c)
    a_i=0
    b_i=0
    c_i=0
    answer_i=0
    answer_len = len(answer)

    while(answer_i<answer_len):
        if answer[answer_i]==a[a_i]:
            result[0]['cnt']+=1
        if answer[answer_i]==b[b_i]:
            result[1]['cnt']+=1
        if answer[answer_i]==c[c_i]:
            result[2]['cnt']+=1
        answer_i+=1
        a_i+=1
        b_i+=1
        c_i+=1
        if a_i==a_len:
            a_i=0
        if b_i==b_len:
            b_i=0
        if c_i==c_len:
            c_i=0
    return result

def solution(answer):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    result = [
        {
            'name':1,
            'cnt':0
        },
        {
            'name':2,
            'cnt':0
        },
        {
            'name':3,
            'cnt':0
        }
    ]
    result = score(a,b,c,answer,result)
    result = sorted(result, key = lambda x:x['cnt'], reverse=True)
    keys=[]
    if result[0]['cnt']==result[1]['cnt']==result[2]['cnt']:
        for i in range(3):
            keys.append(result[i]['name'])
        return keys
    elif result[0]['cnt']==result[1]['cnt']:
        for i in range(2):
            keys.append(result[i]['name'])
        return keys
    else:
        keys.append(result[0]['name'])
        return keys
solution([3, 3, 1, 1, 1, 1, 2, 3, 4, 5])