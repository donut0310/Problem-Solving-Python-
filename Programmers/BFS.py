from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
    return visited
  
graph_list = {1: [2, 3,4],
              2: [5,6],
              3: [6,7],
              4: [8],
              5: [6],
              6: [8],
              7:[],
              8:[]
              }
root_node = 1
print(BFS_with_adj_list(graph_list, root_node))
