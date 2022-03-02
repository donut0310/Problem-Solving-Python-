from collections import defaultdict
from collections import deque

## 재귀 풀이 => 테케 1,2번 실패
# def dfs(v,answer,graph,current,cnt):
#     if len(graph[v])==0:
#         print(v,graph,cnt,current)
#         return
#         if cnt>1:
#             graph[current].append(v)
#             cnt+=1
#             return answer,graph
#     answer.append(v)
#     cnt-=1
#     while len(graph[v]):
#         next_node=graph[v].popleft()
#         dfs(next_node,answer,graph,v,cnt)
#     return answer,graph

# def make_adjlist(tickets):
#     graph = defaultdict(deque)
#     for t in tickets:
#         graph[t[0]].append(t[1])
#     return graph

# def solution(tickets):
#     graph = make_adjlist(tickets)
#     for i in graph.keys():
#         adjList = list(graph[i])
#         adjList.sort()
#         graph[i]=deque(adjList)

#     answer=[]
#     start = 'ICN'
#     cnt = len(tickets)+1
#     dfs('ICN',answer,graph,start,cnt)
#     return answer


# 스택 풀이
def make_adjlist(tickets):
    adjlist = defaultdict(list)
    for t in tickets:
        adjlist[t[0]].append(t[1])
    return adjlist

# def solution(tickets): # 테케 1,2 실패
#     answer=[]
#     # 출발지 고정
#     stack=deque(['ICN'])
#     adjlist = make_adjlist(tickets)
#     path = len(tickets)
#     visited=[]
#     # sort
#     for i in adjlist.keys():
#         adjlist[i].sort(key=lambda x:x[0],reverse=True)
#     # keys
#     keys = adjlist.keys()
#     print(adjlist)
#     while path:
#         t=stack.pop()
#         if t in keys:
#             if len(adjlist[t]) and path:
#                 answer.append(t)
#                 if t not in visited:
#                     stack.extend(adjlist[t])
#                     visited.append(t)
#                 adjlist[t].pop()
#             elif not len(adjlist[t]) and path:
#                 stack.appendleft(t)
#         path-=1
#         print(stack)
#         print(answer)
#     answer.extend(stack)
#     return answer

def solution(tickets):
    adjlist = make_adjlist(tickets)
    for i in adjlist.keys():
        adjlist[i].sort(reverse=True)

    answer=[]
    stack=['ICN']
    while stack:
        tmp=stack[-1]
        if adjlist[tmp]:
            stack.append(adjlist[tmp].pop())
        else:
            answer.append(stack.pop())
    return answer[::-1]
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]])) #["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"]
# print(solution([['ICN', 'B'], ['B', 'C'], ['C', 'ICN'], ['ICN', 'D'], ['ICN', 'E'], ['E', 'F']]))

# print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]))#["ICN", "B", "ICN", "A", "D", "A"]
# print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
#["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]

# DFS 구현을 재귀와 스택으로 구현해봤는데 둘다 테케 1,2번을 통과하지 못했다.
# 기존 방식대로 재귀와 스택으론 해결할 수 없었다.
# ICN을 기준으로 각 정점마다 방문하지 않은경우 인접노드들을 스택에 쌓아 올리고 
# 하나씩 pop하면서 경로탐색을 하였는데 문제의 제약조건들을 만족시키기 힘들었다.

# 참고 풀이
# 반복문마다 스택의 가장 상단 노드를 기준으로 각 정점에서 갈 수 있는 경로가 있으면 
# 해당 노드들 중 사전순으로 빠른 노드를 스택에 삽입 후 인접리스트에서 pop을 시키고
# 갈 수 있는 경로가 없다면 answer 리스트에 삽입 시킨다.
# 이 경우 스택의 가장 상단 노드를 기준으로 갈 수 있는 경로들을 우선 스택에 삽입시키기 때문에
# 문제의 조건인 돌아오는 길이 없는 경우 다음 연결된 노드를 찾아갈 수 있음을 만족한다.
# 스택이 비어있을 때 까지 반복하며 모든 경로가 탐색된 후에는 answer를 역전시켜 반환한다.
# 단순한 DFS로 생각하고 풀었다가 크게 막혔던 문제였다.
