import requests
from bs4 import BeautifulSoup

# 접속할 사이트(웹 서버) 주소
url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D'
# 사이트(웹 서버)로 요청(request)를 보냄
html = requests.get(url).text.strip()  # 요청의 결과(응답, response - HTML)를 저장
print(html[0:100])

# HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
soup = BeautifulSoup(html, 'html5lib')
for link in soup('a'):
    print(link.get('href'))

print('\n============')

for class1 in soup(class_ = 'f_link_b'):
    print(class1.get('href'))

print('\n============')
# 관심 있는 링크(뉴스 링크)들만 찾을 수 있는 방법을 고민 (주말 동안)

div_coll_cont = soup.find_all(class_ = 'coll_cont')
print(len(div_coll_cont))

# HTML 하위 요소(sub/child element)를 찾는 방법
# 1) parent_selector > child_selector
#   div > ul > li
#   .coll_cont > #clusterResultUL .fst

# 2) ancestor_selector descendant_selector
#   div li  (div 의 자손 요소들 중 li들)
#   .coll_cont .fst (클래스 .coll_cont 요소의 자손 요소들 중 클래스가 fst 인 요소들)

# soup.select(css_selector): soup 객체에서 CSS 선택자로 요소들을 찾는 방법

news_link = soup.select('.coll_cont ul li a.f_link_b')

link_list = [i.get('href') for i in news_link]
print(link_list)
print()

for id, x in enumerate(link_list, 1):
    print(id, x)





