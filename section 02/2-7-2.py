from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="https://finance.naver.com/sise/"
res=req.urlopen(url).read().decode('cp949')
soup = BeautifulSoup(res,"html.parser")


top = soup.select("#siselist_tab_0 > tr")




# for e in top :
#     print(e)

# for e in top:
#     print(e.find("a"))



i=1



print('Top 10 종목명 출력')
for v,e in enumerate(top) :
    if e.find("a") is not None:
        print(i, e.select_one(".tltle").string, " = ", e.select_one(":nth-of-type(5)").string)
        i+=1


# for i,e in enumerate(top) :
#     print(i+1, e.string)
