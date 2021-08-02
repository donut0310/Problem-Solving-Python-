def solution(price, money, count):
    total = 0
    for i in range(1,count+1):
        total += i * price
    if money<total:
        return total-money
    else:
        return 0
