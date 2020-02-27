from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="https://finance.naver.com/sise/"
res=req.urlopen(url).read().decode('cp949')
soup = BeautifulSoup(res,"html.parser")


top = soup.select("ul#popularItemList>li")


i=1


print('Top 10 종목명 출력')
for v,e in enumerate(top) :
    print(i, e.find("a").string,"=", e.find("span").string)
    i+=1
