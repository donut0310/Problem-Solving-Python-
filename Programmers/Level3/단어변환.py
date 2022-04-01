from collections import deque

def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]    
    queue = deque([(begin,0)])
    #BFS
    while queue:
        tmp = queue.popleft()
        if tmp[0]==target: return tmp[1]
        for index,word in enumerate(words):
            cnt=0
            for i in range(len(word)):
                if tmp[0][i] != word[i]: cnt+=1
                if cnt>1: break
            if cnt==1 and not visited[index]:
                visited[index]=1
                queue.append((word,tmp[1]+1))
    return 0

print(solution('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit','cog',["hot", "dot", "dog", "lot", "log"]))

'''
풀이
문제 조건상 한번에 한 개의 알파벳 글자만 바꿀 수 있기 때문에 각 실행에서 큐의 첫번째 원소를 기준으로
words배열에 있는 값들과 비교를 해서 글자수가 하나만 다른 경우를 찾고, 방문 여부를 확인 후 queue에 새로 삽입한다.
이때 각 단어들은 이전단어의 다음단계이기 때문에 거리를 +1씩 늘려준다.
큐가 남아있을때까지 반복하며 target을 찾으면 그때의 거리를 반환한다.
'''