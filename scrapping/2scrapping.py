from bs4 import BeautifulSoup as soup
import requests
import io
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import re

page_url = "https://mubasher.aljazeera.net/tag/jerusalem/"
driver = webdriver.Chrome("C:/Users/abderrahman/chromedriver")
driver.get(page_url)


def lastItem():
    return '//*[@id="news-feed-container"]/article[10]'


def toBeClicked():
    return '//*[@id="news-feed-container"]/button'

def coockies():
    time.sleep(3)
    print("--------------Accepting Coockies--------------")
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

def scrollScrapAndClickForMoreNews(driver):
    time.sleep(4)
    print("--------------Scrolling Down--------------")
    driver.execute_script("arguments[0].scrollIntoView()", driver.find_element_by_xpath(lastItem()))
    time.sleep(4)
    print("--------------Clicking for more news--------------")
    driver.find_element_by_xpath(toBeClicked()).click()
    time.sleep(12)


def scrapNnews(nNews, driver):
    for i in range(nNews):
        scrollScrapAndClickForMoreNews(driver)
        print("News are scrapped")


coockies()
scrapNnews(15, driver)

print("--------------Writing results in a txt file--------------")
uClient = requests.get(page_url)
page_soup = soup(driver.page_source, "html.parser")
uClient.close()
with io.open("FakeNews.txt", "a", encoding="utf-8") as f:
    buffer = page_soup.findAll("div", {"class": "gc__excerpt"})
    for b in buffer:
        my_new_string = re.sub(
            r'[^\d\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+',
            ' ', b.find("p").text.strip())
        f.write(my_new_string + ";" + "REAL" + "\n")

print("--------------Finished--------------")
