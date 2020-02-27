import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

imgUrl="https://www.woodkorea.co.kr/news/photo/201911/35141_39356_831.png"
htmlUrl="https://www.google.com/"

savePath1="D:/gms/Atom/test1.jpg"
savePath2="D:/gms/Atom/index.html"

# f=dw.urlopen(imgUrl).read()
f2=dw.urlopen(htmlUrl).read()

# write : 저장
# read : 읽기
# a:add(=append)
# saveFile1 = open(savePath1, 'wb')
# saveFile1.write(f)
# saveFile1.close()

with open(savePath2, 'wb') as savePath2:
    savePath2.write(f2)

print("다운로드완료!")
