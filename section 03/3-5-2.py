from bs4 import BeautifulSoup
import requests
import json
import sys
import io
import urllib.request as req
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


# Fake header
ua=UserAgent()

# Header선언
headers={
    'User-Agent': ua.ie,
    'Referer':'http://finance.daum.net/'

}


# 다음 주식 요청 url
url="https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
# 응답데이터 확인(Json Data)
print(res)

# 응답데이터 res > json변환 및 data값 저장
rank_json=json.load(res)['data']

# 중간확인
print(rank_json)


# BeautifulSoup 선언
soup=BeautifulSoup(res,"html.parser")
article=soup.select('#boxMarketTrend > div.box_contents > div:nth-child(1) > table > tr')
# print(article.text)

for i in article :
    print(i)


# 확인
# print(res)
