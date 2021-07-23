def solution(s):
    obj=[{'zero':'0'},{'one':'1'},{'two':'2'},{'three':'3'},{'four':'4'},{'five':'5'},{'six':'6'},{'seven':'7'},{'eight':'8'},{'nine':'9'}]
    obj2=['0','1','2','3','4','5','6','7','8','9']
    answer = []

    while(len(s)>0):
        if s[0] not in obj2:
            for i in obj:
                item = list(i.keys())[0]
                item_len = len(item)
                if item == s[:item_len]:
                    answer.append(i[item])
                    s=s[item_len:]
        else:
            index = obj2.index(s[0])
            answer.append(str(index))
            s=s[1:]
    answer = ''.join(answer)
    return int(answer)
solution('one4seveneight')
solution('23four5six7')
solution('2three45sixseven')
solution('123')