def make_new_num(num):
    tmp = num
    while num > 0:
        tmp += num % 10
        num //= 10
    return tmp

def solution():
    arr = [0] * 10001

    for i in range(1, 10001):
        num = make_new_num(i)
        if num < 10001: arr[num] = 1
    
    for i in range(1, 10001):
        if not arr[i]: print(i)

solution()