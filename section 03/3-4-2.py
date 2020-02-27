import requests, json
import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req


sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")


# 로그인 유저정보
LOGIN_INFO = {
    'user_id' : 'gms0417',
    'user_pw' : 'rhkraltjs@33'
}


# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
                    # login_proc 에 로그인 정보가 들어감

    # HTML 소스 확인
    # print(login_req.text)

    # HTTP header 불러오기
    # print(login_req.headers)

    # Response 정상확인
    if login_req.status_code == 200 and login_req.ok :
        print("로그인성공")


    # 권한이 필요한 게시판 글 가져오기
    url = s.get('https://mypi.ruliweb.com/mypi.htm?num=8035&nid=7231')
    soup = BeautifulSoup(url.text, "html.parser")
    doc = soup.select("div.story > p")

    for i,e in enumerate(doc) :
        print(e.string)
