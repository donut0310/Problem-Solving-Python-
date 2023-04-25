from collections import defaultdict

def time_converter(date):
    y, m, d = map(int, date.split('.'))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    answer = []
    terms_info = defaultdict(int)
    
    # 약관 정보 딕셔너리 초기화
    for term in terms:
        t, m = term.split(' ')
        terms_info[t] = int(m)
    
    # 파기할 개인정보 탐색
    today = time_converter(today)
    
    for i, privacy in enumerate(privacies):
        date, term = privacy.split(' ')

        if time_converter(date) + terms_info[term] * 28 <= today:
            answer.append(i+1)
            
    return answer