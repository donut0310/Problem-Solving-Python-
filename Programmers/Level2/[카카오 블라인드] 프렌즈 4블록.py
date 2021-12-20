def solution(m, n, board):
    answer = 0
    board_c=[]
    # 문자열 나누기 => [['A',B','C'],['B','C','E']]
    for i in board:
        arr=[]
        for j in i:
            arr.append(j)
        board_c.append(arr)

    while True:
        flag=set() # 터뜨릴 블록의 위치정보를 저장 flag=[(1,2),(0,0)...]
        for i in range(m-1):
            for j in range(n-1):
                if board_c[i][j]=='0': pass
                elif board_c[i][j]==board_c[i][j+1]==board_c[i+1][j]==board_c[i+1][j+1]:
                    flag.add((i,j))
                    flag.add((i,j+1))
                    flag.add((i+1,j))
                    flag.add((i+1,j+1))
        if len(flag)==0: return answer # 더 이상 터뜨릴 블록이 없는 경우 정답 리턴
        answer+=len(flag)
        # flag에 저장된 터뜨릴 블록들을 '0'으로 할당
        for i,j in flag:
            board_c[i][j]='0'
        
        # 열을 기준으로 터뜨린 블록들의 위치를 남은 블록들로 채워줌
        for i in range(n):
            cnt=0
            for j in range(m-1,0,-1):
                if board_c[j][i]=='0':
                    cnt+=1
                    if board_c[j-1][i]!='0':
                        board_c[j-1][i],board_c[j-1+cnt][i]=board_c[j-1+cnt][i],board_c[j-1][i]
                        cnt-=1
                    
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))