import requests
from bs4 import BeautifulSoup

url1 = 'https://search.naver.com/search.naver?where=nexearch&query=%EC%86%90%ED%9D%A5%EB%AF%BC+%EA%B3%A8&sm=top_lve.agallgrpmamsi0en0sp0&x_nxpr-front=all01-2&ie=utf8'
url2 = 'https://www.genie.co.kr/chart/top200'
url3 = 'https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%EA%B9%80%EA%B1%B4%EB%AA%A8'



html = requests.get(url2).text
print(html)

# print('\n===============\n')
#
# soup = BeautifulSoup(html, 'html.parser')
#
#
# for i in soup.find(class_= 'list-wrap').find_all('tr'):
#     for tag in i.find_all(class_ = 'title ellipsis'):
#         print(tag)