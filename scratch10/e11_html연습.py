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


def search_news(keyword, page_no):

    start_page = 1
    final_page = page_no

    print('검색 단어 :', keyword)

    link_list = []
    title_list = []
    for i in range(1, final_page + 1):
        url = f'https://search.daum.net/search?w=news&DA=PGD'
        req_params = {
            'q': keyword,
            'p': i
        }
        html = requests.get(url, params = req_params).text.strip()
        soup = BeautifulSoup(html, 'html5lib')
        news_link = soup.select('.coll_cont .f_link_b')

        for link in news_link:
            link_list.append(link.get('href'))
            title_list.append(link.text)

    df = pd.DataFrame({
        '제목': title_list,
        '링크': link_list
    })

    return df


if __name__ == '__main__':
    list = search_news('머신러닝', 10)
    print(list)
    print(list.shape)








