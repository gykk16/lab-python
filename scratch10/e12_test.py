import pandas as pd
import requests
from bs4 import BeautifulSoup




keyword = '머신러닝'
search_pages = 5
url = 'http://search.hani.co.kr/Search?command=query&media=news&sort=d&period=all'
for page in range(search_pages):
    print(f'\n\n====== Page {page + 1} =======')
    req_params = {
        'keyword': keyword,
        'pageseq': page
    }
    html = requests.get(url, params = req_params).text.strip()
    soup = BeautifulSoup(html, 'html5lib')

    for date in soup.select('ul.search-result-list li dl dd.date'):
        news_date = date.text.strip()


    for i in soup.select('.search-result-list li dt a'):
        news_url = i.get('href')
        news_title = i.text

        html2 = requests.get(news_url).text.strip()
        soup2 = BeautifulSoup(html2, 'html5lib')

        for text in soup2.select('.article-text > .article-text-font-size > .text'):
            news_text = text.get_text().strip()
            print(f'{news_title}, {news_date}, {news_url} \n\n {news_text} \n\n'
                  f'=======================================================\n'
                  f'=======================================================\n\n')