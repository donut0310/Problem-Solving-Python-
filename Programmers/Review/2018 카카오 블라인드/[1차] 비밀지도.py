def to_binary(num, n):
    result = ''
    while num > 0:
        result += str(num % 2)
        num //= 2

    tmp = n - len(result)
    result += (tmp * '0')

    return result[::-1]

def sum_rows(row1, row2):
    result = ''

    for i in range(len(row1)):
        if row1[i] == '1' or row2[i] == '1': result += '#'
        else: result += ' '

    return result

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        row1, row2 = to_binary(arr1[i], n), to_binary(arr2[i], n)
        answer.append(sum_rows(row1, row2))

    return answer

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))  # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, 	[46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])) # ["######", "### #", "## ##", " #### ", " #####", "### # "]