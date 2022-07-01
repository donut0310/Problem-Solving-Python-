import re
from collections import defaultdict

def solution(word, pages):
    answer = 0
    word = word.lower()
    basic_score = defaultdict(int) # 기본점수
    externals = defaultdict(list) # 각 url 별 외부링크 정보
    
    for page in pages:
        url = re.search(r'(<meta property.+content=")(https://.*)"/>', page).group(2) # url 검색, () 그룹핑
        ex_url = re.findall(r'<a href="https://\S*"', page) # 외부 url 검색
        cnt=0
        for w in re.findall(r'[a-z]+',page.lower()):
            if w==word: cnt+=1
        basic_score[url] = cnt # 기본 점수 저장
        [externals[url].append(i[9:-1]) for i in ex_url] # 각 url 별 외부링크 저장

    # 링크점수 계산
    link_score = defaultdict(int)
    for url,links in externals.items():
        score = basic_score[url]
        for link in links:
            link_score[link] += score/len(externals[url])

    results = []
    cnt=0
    for url,score in basic_score.items():
        results.append((cnt,score+link_score[url]))
        cnt+=1

    answer = sorted(results,key=lambda x:(-x[1],x[0]))[0][0]
    return answer

print(solution('blind',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
)) # 0

print(solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
)) # 1

'''
url => <meta property="og:url" content="https://careers.kakao.com/index" />
외부링크 => <a href="https://careers.kakao.com/index">
모든 url => https:// 로 시작
word의 길이 1~12
검색어 대소문자 무시
단어 단위 비교, abc!=abcde, abc, abc@abc abc는 3개 일치로 판단
매칭점수 같을 시 index번호로 오름차순
기본점수 = 단어 매칭 개수
외부 링크 수,
링크 점수 => 해당 웹페이지로 링크 걸린 다른 웹페이지의 기본점수 % 외부 링크 수의 총합

매칭 점수 => 기본점수 + 링크점수의 합
dict => url: int 
'''
