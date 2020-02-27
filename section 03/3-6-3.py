import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

#import time
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


# 1. 옵션적용
firefox_option=Options()
firefox_option.add_argument("--headless")   # CLI

driver = webdriver.Firefox(executable_path='D:/Atom/section 03/webdriver/firefox/geckodriver')

# 2. GUI
driver.set_window_size(1920,1280)
driver.get('https://google.com')
time.sleep(5)
driver.save_screenshot("D:/Atom/section 03/webdriver/firefox/website1.png")
