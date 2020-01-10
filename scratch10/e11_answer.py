'''
웹 주소(URL, URI) 의 형식
    프로토콜://서버주소[:포트번호]/경로?퀴리스트링
    https://www.naver.com/
    https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N

    쿼리 스트링(query string): 클라이언트(브라우저)가 서버로 보내는 정보
        param이름=param값 형식으로 작성
        파라미터가 여러개일 경우에는 & 로 파라미터들을 구분

다음에서 '머신러닝' 으로 검색한 기사 100개의 URL 주소와 기사 제목을 출력

'''
import requests
import pandas as pd
from bs4 import BeautifulSoup


def daum_search(keyword):
    url = 'https://search.daum.net/search?w=news&DA=PGD'
    for page in range(1, 11):
        print(f'====== Page {page} =======')
        req_params = {
            'q': keyword,
            'p': page
        }
        response = requests.get(url, params = req_params)
        html = response.text.strip()

        soup = BeautifulSoup(html, 'html5lib')
        news_link = soup.select('.coll_cont a.f_link_b')
        for link in news_link:
            # HTML 요소(element)의 href 속성(attribute) 값을 읽음.
            news_url = link.get('href')
            # HTML 요소가 가지고 있는 컨텐트 문자열
            news_title = link.text
            print(news_title, news_url)
        print(f'====== Page {page} =======')


if __name__ == '__main__':
    # url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&p='
    url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD'
    for page in range(1, 11):
        print(f'====== Page {page} =======')
        # page_url = url + str(page)
        # print(page_url)

        # 해당 페이지 URL 주소로 GET 방식 요청(request)을 보내고,
        # 서버에서 보낸 응답(response)을 문자열로 처리
        # html = requests.get(page_url).text.strip()
        response = requests.get(url, params = {'p': page})
        # requests.get(url, params={key: value}):
        #   params 의 내용을 url 의 query string 의 파라미터로 추가해줌
        html = response.text.strip()

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html, 'html5lib')

        news_link = soup.select('.coll_cont a.f_link_b')
        for link in news_link:
            # HTML 요소(element)의 href 속성(attribute) 값을 읽음.
            news_url = link.get('href')
            # HTML 요소가 가지고 있는 컨텐트 문자열
            news_title = link.text
            print(news_title, news_url)
        print(f'====== Page {page} =======')
