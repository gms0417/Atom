import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')



driver = webdriver.PhantomJS('D:/Atom/section 03/webdriver/phantomjs/phantomjs')
driver.implicitly_wait(5)
driver.get('http://google.com')
driver.save_screenshot("D:/Atom/section 03/webdriver/phantomjs/website1.png")


driver.implicitly_wait(5)
driver.get('http://daum.net')
driver.save_screenshot("D:/Atom/section 03/webdriver/phantomjs/website2.png")
print("스크린샷 완료")
