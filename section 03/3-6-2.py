import sys
import io
from selenium import webdriver
import time

#import time
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


driver = webdriver.Chrome('D:/Atom/section 03/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.get('https://google.com')
time.sleep(5)
driver.save_screenshot("D:/Atom/section 03/webdriver/chrome/website1.png")

driver.get('https://daum.net')
driver.save_screenshot("D:/Atom/section 03/webdriver/chrome/website2.png")
driver.quit()
print("스크린샷 완료")
