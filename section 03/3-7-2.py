import sys
import io
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

class NcafeWriteAtt:
    def __init__(self) :
        self.driver = webdriver.Chrome(executable_path=r"D:/Atom/section 03/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)


    def writeAttendCheck(self) :
        # 로그인
        self.driver.get("hhttps://cafe.naver.com/hby")
        pyperclip.copy('아이디')
        self.driver.find_element_by_name('id').click()
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy('비밀번호')
        self.driver.find_element_by_name('pw').click()
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        self.driver.find_element_by_xpath('//*[@id="gnb_login_button"]').click()
        time.sleep(3)


        self.driver.implicitly_wait(5)
        self.driver.get("https://cafe.naver.com/CafeMemberViewTab.nhn?defaultSearch.clubid=10135947")
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame('cafe_main')

        self.driver.implicitly_wait(1)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        #선택자 추출
        return soup.select('div.ellipsis.m-tcol-c')
        time.sleep(3)


    # 네이버 회원 리스트 출력 및 저장
    def printMemberList(self,list):
        f = open("D:/Atom/section 03/webdriver/chrome/chromedriver/MemberList.txt", wt)
        for i in list :
            f.write(i.string.strip()+"\n")
            print(i.string.strip())
        f.close()


    #소멸자 (생성자를 닫아주는 역활)
    def __del__(self) :
        self.driver.quit()
        print("Remove driver Object")

# 실행
if __name__ == '__main__' :
    # 객체 생성
    a = NcafeWriteAtt()
    # 시작 시간
    start_time = time.time()    #현재시간
    # 프로그램 실행
    a.printMemberList(a.getMemberList())
    # 종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    time.sleep(10)
    # 객체 소멸
    del a




ns = NcafeWriteAtt()
ns.writeAttendCheck()
