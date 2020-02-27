import requests, json
import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req


sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")


with requests.Session() as s:
    # 게시글 가져오기
    post_one=s.get('https://bbs.ruliweb.com/market/board/1020/read/37546')
    # print(post_one.text)

    # 예외 발생
    post_one.raise_for_status()

    # 예외발생 print
    print(post_one.status_code)
    print(post_one.ok)


    # Beautifulsoup 선언 및 확인
    soup = BeautifulSoup(post_one.text, "html.parser")

    # 문서만 추출 및 확인 (select)
    doc = soup.select("#board_read > div > div.board_main > div.board_main_view > div.view_content > div > p")
    # print(doc)

    # # string 처리 (for)
    for i,e in enumerate(doc) :
        print(e.string)
