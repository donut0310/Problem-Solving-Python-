import math

def solution(n, s, a, b, fares):
    adj_matrix = [[math.inf] * (n+1) for _ in range(n+1)]

    for v1, v2, w in fares:
        adj_matrix[v1][v2] = w
        adj_matrix[v2][v1] = w
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])

    answer = adj_matrix[s][a] + adj_matrix[s][b]

    for i in range(1, n+1):
        if i==a:
            answer = min(adj_matrix[s][a] + adj_matrix[a][b], answer)
        elif i==b:
            answer = min(adj_matrix[s][b] + adj_matrix[b][a], answer)
        else: 
            answer = min(adj_matrix[s][i] + adj_matrix[i][a] + adj_matrix[i][b], answer)
    return answer

# print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# 82
# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# 14
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
# 18