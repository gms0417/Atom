from bs4 import BeautifulSoup
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")
html = """
<html><body>
    <ul>
        <li id="naver"><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html,"html.parser")
# li=soup.select_one("li#naver").string
# li2=soup.find("li", string="naver").string
# li3=soup.find(id="naver").string
#     # select_one과 동일하게 바로 String처리가 가능하다.
# print(li)
# print(li2)
# print(li3)

li=soup.find_all(href=re.compile(r"^http://"))
    # ^ : https://로 시작하는
li2=soup.find_all(href=re.compile(r"da"))

for a in li:
    print(a.attrs['href'])

print(li2)
