def pick(board, index, stack):
    size = len(board)
    for i in range(size):
        if board[i][index] != 0:
            stack.append(board[i][index])
            board[i][index]=0
            break
    return stack

def check(stack,answer):
    stackLen = len(stack)
    if stackLen<=1:
        return stack,answer
    if stack[stackLen-1]==stack[stackLen-2]:
        stack.pop()
        stack.pop()
        answer+=2
    return stack,answer

def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        stack = pick(board,i-1,stack)
        stack, answer = check(stack,answer)
    print(board)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])

# 00000
# 00103
# 02501
# 42442
# 35131

# 4 3 1 1 3 2 4
# 4 2 4