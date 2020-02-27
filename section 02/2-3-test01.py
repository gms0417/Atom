import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

imgUrl1="https://img.khan.co.kr/news/2019/11/29/l_2019112901003607500286631.jpg"

savePath1="D:/gms/Atom/img01.jpg"

f1=dw.urlopen(imgUrl1).read()


with open(savePath1, 'wb') as savePath1:
    savePath1.write(f1)


print("다운로드완료!")
