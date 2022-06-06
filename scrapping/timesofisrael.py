from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq  # Web client
import io
from selenium import webdriver
import time
import re

from selenium.webdriver.common.by import By

page_url = "https://ar.timesofisrael.com/topic/%d8%a7%d9%84%d9%82%d8%af%d8%b3-%d8%a7%d9%84%d9%82%d8%af%d9%8a%d9%85%d8%a9/"
driver = webdriver.Chrome("C:/Users/abderrahman/chromedriver")
driver.get(page_url)


def lastItem():
    return '/html/body/footer'


def toBeClicked(n):
    return f'/html/body/div[1]/div[3]/section[2]/div[{n}]/a'

def coockies():
    time.sleep(2)
    print("--------------Accepting Coockies--------------")
    driver.find_element(By.XPATH, '/html/body/div[3]/div/a').click()


def scrollScrapAndClickForMoreNews(driver):
    time.sleep(4)
    print("--------------Scrolling Down--------------")
    driver.execute_script("arguments[0].scrollIntoView()", driver.find_element(By.XPATH, lastItem()))
    time.sleep(4)
    print("--------------Clicking for more news--------------")
    n = 16
    while True:
        try:
            print(f'n = {n}')
            driver.find_element(By.XPATH, toBeClicked(n)).click()
            break
        except:
            n = n + 1
            pass



def scrapNnews(nNews, driver):
    for i in range(nNews):
        scrollScrapAndClickForMoreNews(driver)
        print("scrolling finished")


# coockies()
scrapNnews(7, driver)

print("--------------Writing results in a txt file--------------")
uClient = uReq(page_url)
page_soup = soup(driver.page_source, "html.parser")
uClient.close()
with io.open("FakeNews.txt", "a", encoding="utf-8") as f:
    f.write("text" + ";" + "label" + "\n")
    buffer = page_soup.findAll("div", {"class": "headline"})
    for b in buffer:
        my_new_string = re.sub(
            r'[^\d\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+',
            ' ', b.find('a').text.strip())
        f.write(my_new_string + ";" + "FAKE" + "\n")

print("--------------Finished--------------")
