def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: # 맨 왼쪽 인덱스
                triangle[i][j] += triangle[i-1][0]
            elif j == len(triangle[i]) - 1: # 맨 오른쪽 인덱스
                triangle[i][j] += triangle[i-1][-1]
            else: 
                triangle[i][j] += max(triangle[i-1][j-1:j+1])

            answer = max(triangle[i][j], answer)    
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

'''
<풀이>
맨 왼쪽과 맨 오른쪽 인덱스는 각각의 윗 층에서의 맨 왼쪽과 맨 오른쪽 인덱스의 값에 자신을 더한 값이 된다.
내부의 원소들은 자신이 있는 층(i)에서 자신의 인덱스(j)를 기준으로 윗층에서(i-1) (j-1 ~ j) 까지의 두 원소 중 큰 값과의 더한 값을 가지게 된다.
'''
