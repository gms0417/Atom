from bs4 import BeautifulSoup
import requests
import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


driver = webdriver.Chrome('D:/Atom/section 03/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.implicitly_wait(3)
driver.get('https://www.wishket.com/mywishket/partners/')
time.sleep(5)
driver.find_element_by_name('identification').send_keys('gms0417')
driver.implicitly_wait(3)

driver.find_element_by_name('password').send_keys('rhkraltjs@33')
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="submit"]').click()
