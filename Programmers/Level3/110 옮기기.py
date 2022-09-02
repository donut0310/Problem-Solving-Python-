def solution(s):
    answer = []

    for word in s:
        tmp, cnt = '', 0
    
        for i in word:
            tmp += i
            if tmp[-3:] == '110':
                cnt += 1
                tmp = tmp[:-3]

        target = '110' * cnt

        for j in range(len(tmp)-1, -1, -1):
            if tmp[j] == '0':
                tmp = tmp[:j + 1] + target + tmp[j+1:]
                break
        else: tmp = target + tmp
        answer.append(tmp)
    return answer

print(solution(["1110", "100111100", "0111111010"])) # ["1101","100110110","0110110111"]

'''
<풀이>
1. tmp 임시변수에 문자열의 값을 하나씩 삽입하면서 삽입된 위치를 포함해 뒤로 3글자가 '110'에 해당하는지 확인한다.
2. '110'에 포함된다면, '110'의 개수를 cnt 변수에 갱신하고, tmp 변수에서 위 3글자를 잘라낸다.
3. target변수에 cnt 개수만큼 '110'을 확장한 값을 저장한다.
4. 완성된 tmp 변수에 target을 삽입해야 하는데, 삽입했을 때 사전순으로 오름차순인 경우를 만들어야하므로,
    0보다는 무조건 뒤에, 1보다는 앞에 위치해야한다. 
5. 따라서, 주어진 tmp 변수를 뒤에서부터 탐색하며 처음으로 0이 나오는 인덱스를 확인하고, 해당 인덱스 바로 뒤에 target 변수를 붙여준다.
6. 예외로, tmp변수가 1로만 이루어진 경우가 있기 때문에, 5과정에서 break가 걸리지 않는다면 target 변수 뒤에 tmp 변수를 붙여준다.
'''
