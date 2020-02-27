import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#import time
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

chrome_option=Options()
chrome_option.add_argument("--headless")   # CLI

driver = webdriver.Chrome(chrome_options=chrome_option, executable_path=r'D:/Atom/section 03/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.get('https://daum.net')
driver.save_screenshot("D:/Atom/section 03/webdriver/chrome/website5.jpg")
driver.quit()
print("스크린샷 완료")
