from bs4 import BeautifulSoup
import sys
import io
import re
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

fp = open("D:/Atom/section 02/food-list.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

# print(soup)


# 양주출력
print(soup.select("li:nth-of-type(4)")[1].string)
print(soup.select_one("#ac-list > li:nth-of-type(4)").string)
print(soup.select("#ac-list > li[data-lo='cn']")[0].string)
print(soup.select("#ac-list > li.alcohol.high")[0].string)

# 삼겹살 출력
print(soup.select("li:nth-of-type(3)")[0].string)
print(soup.select_one("#fd-list > li:nth-of-type(3)").string)
print(soup.select("#fd-list > li[data-lo='ko']")[1].string)
print(soup.select("#fd-list > li.food.hot")[1].string)

# 양주 출력
param={"data-lo":"cn", "class":"alcohol"}
print(soup.find("li", param).string)
print(soup.find(id="ac-list").find("li", param).string)


# 삼겹살 find
for ac in soup.find_all("li") :
    if ac['data-lo']=='us' :
        print('data-lo==us : ', ac.string)


# find_all 필터링=ko
for fd in soup.find_all("li") :
    if fd['data-lo']=='ko' :
        print('data-lo==ko : ', fd.string)
