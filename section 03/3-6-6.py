import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import requests
from selenium.webdriver.common.by import By

#import time
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# chrome_option=Options()
# chrome_option.add_argument("--headless")   # CLI

        # 요청
driver = webdriver.Chrome(executable_path=r'D:/Atom/section 03/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.get('http://www.encar.com/index.do')
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath("//*[@id='indexSch1']/div[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='sr_photo']/li[1]/a/span[1]/span[1]/span").click()
