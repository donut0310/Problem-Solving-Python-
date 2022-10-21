def solution(answers):
    answer = []
    player = ['12345', '21232425', '3311224455']

    for i in range(len(player)):
        m, d = divmod(len(answers), len(player[i]))
        player[i] = m * player[i] + player[i][:d]
    
    
    tmp = []
    maxi = 0
    for i, p in enumerate(player):
        cnt = 0

        for j in range(len(answers)):
            if answers[j] == int(p[j]): cnt += 1
        maxi = max(maxi, cnt)
        tmp.append((i, cnt))    
    
    tmp.sort(key=lambda x:(-x[1], x[0]))
    for i, cnt in tmp:
        if cnt == maxi: answer.append(i+1)
        else: break
    return answer