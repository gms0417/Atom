import requests, json
import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req


sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")


with requests.Session() as s:
    url = s.post('https://movie.naver.com/movie/bi/mi/point.nhn?code=161967')
    soup = BeautifulSoup(url.text, "html.parser")
    review = soup.select("div.score_reple")

    for i,e in enumerate(review) :
        print(i+1, e.select_one("p").string)
