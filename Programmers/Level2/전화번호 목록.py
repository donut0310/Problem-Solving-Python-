def solution(phone_book):
    phone_book.sort()

    # 사전 형식으로 정렬 후 바로 뒤의 숫자와 비교했을때 접두어인 경우가 아니라면 그 뒤 모든 숫자와 비교 할 필요가 없음!!
    for i in range(len(phone_book)-1):
            if phone_book[i+1].startswith(phone_book[i]):
                return False
    return True

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])