'''


'''
from icrawler.builtin import GoogleImageCrawler
import os


save_dir = os.path.join('G:' + os.sep, '내 드라이브', 'dev', 'images')
google_crawler = GoogleImageCrawler(storage = {'root_dir': save_dir})


filters = {
    'size': 'large',
    'color': 'color'
}

google_crawler.crawl(keyword = '금요일 짤', max_num = 50)
