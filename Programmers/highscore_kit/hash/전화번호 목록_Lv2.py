from collections import defaultdict

def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x:len(x)) # 전화번호부를 길이별로 오름차순 정렬
    mini, maxi = len(phone_book[0]), len(phone_book[-1]) # 길이가 가장 작은 값과 큰 값을 추출
    p_dict = defaultdict(int) # 전화번호부를 저장할 dictionary 선언

    for phone in phone_book:
        if len(phone) == mini:
            p_dict[phone] += 1
            continue
        
        for i in range(mini, maxi):
            tmp = phone[:i]
            if p_dict[tmp]: return False

        p_dict[phone] += 1
    return answer

print(solution(["119", "97674223", "1195524421"])) # false
