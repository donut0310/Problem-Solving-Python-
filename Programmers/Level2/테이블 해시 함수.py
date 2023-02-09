def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key = lambda x:(x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        data[i] = [data[i][j] % (i+1) for j in range(len(data[i]))]
        if i == row_begin - 1:
            answer = sum(data[i])
        else:
            answer ^= sum(data[i])
        
    return answer
