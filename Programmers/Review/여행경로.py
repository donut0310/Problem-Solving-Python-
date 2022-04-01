from collections import defaultdict

def solution(tickets):
    answer = []
    # 인접 리스트 만들기
    cities = defaultdict(list)
    [cities[i].append(j)for i,j in tickets]
    [cities[i].sort(reverse=True) for i in cities] #알파벳 역순 정렬
    
    #DFS
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        if cities[tmp]: stack.append(cities[tmp].pop())
        else: answer.append(stack.pop())
    return answer[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	)) #["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) #["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution([['ICN','A'],['A','S'],['S','A'],['S','C']])) # ["ICN","A","S","C","A"]

'''
스택의 최상단에 있는 도시를 선택한다.
해당 도시에서 다음 도시로 갈 수 있는 경우엔 스택에 다음 도시를 넣어준다
다음 도시로 갈 수 없는 경우에는 스택의 최상단에 있는 도시를 pop 한 후 answer 배열에 담아준다.
모든 작업이 마무리 된 후 answer배열을 뒤집어주면 제일 먼저 방문한 도시부터 차례대로 정렬되게 된다.
'''