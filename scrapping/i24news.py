import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq  # Web client
import io
from selenium import webdriver
import time
import re

# r = requests.get("https://www.i24news.tv/ar/tags/%D8%A7%D9%84%D9%82%D8%AF%D8%B3")
# bs = soup(r.text, features='html.parser')
# # print(bs.prettify())
# headers = bs.findAll('p', {'class' : 'title'})
news = []
# for i in headers:
#     if len(i.get_text().strip()) > 15:
#         news.append(i.get_text().strip())

for page_number in range(30, 100):
    print(page_number)
    r = requests.get("https://www.i24news.tv/ar/tags/%D8%A7%D9%84%D9%82%D8%AF%D8%B3?page=" + str(page_number))
    time.sleep(3)
    bs = soup(r.text, features='html.parser')
    # print(bs.prettify())
    headers = bs.findAll('p', {'class': 'title'})
    for i in headers:
        print('====> ' + str(i.get_text().strip()))
        if len(i.get_text().strip()) > 15:
            news.append(i.get_text().strip())
    print('len(news)' + str( len(news) ))


with open('./FakeNews.txt',mode='a', encoding='utf8' ) as f:
    for l in news:
        f.write(l + ";FAKE\n")