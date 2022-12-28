def euclid(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def solution():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        arr[i] = abs(arr[i] - s)
    arr = list(set(arr))

    tmp = min(arr)
    for i in range(len(arr)):
        tmp = euclid(arr[i], tmp)

    print(tmp)

solution()