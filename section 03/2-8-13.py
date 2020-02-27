from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

#HTML 가져오기
base="https://search.naver.com/search.naver?where=image&query="
quote=rep.quote_plus("먼치킨")
url=base+quote

res=req.urlopen(url)
savePath = "D:\\imagedown\\"
try:
    if not(os.path.isdir(savePath)) :
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno!=errno.EEXIST:  # 존재한다는 오류 외 나머지
        print("Faild to create directory!!!!")
        raise               # 컴파일하여 폴더 유무를 확인


soup = BeautifulSoup(res, "html.parser")

li_list = soup.select("div.img_area._item > a.thumb._thumb > img")

for i, div in enumerate(li_list,1):
    # print("div = ", div['data-source'])
    fullfilename=os.path.join(savePath, savePath+str(i)+'.jpg')
    # print(fullfilename)
    req.urlretrieve(div['data-source'],fullfilename)

print("다운로드완료")
