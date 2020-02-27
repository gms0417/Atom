from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="https://www.daum.net/"
res=req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")


top = soup.select("div.realtime_part > ol.list_hotissue.issue_row > li")


i=1
print('인기검색어')
for i,e in enumerate(top) :
    print(i+1, e.select_one("a").string)
    
