import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

moveUrl="https://tvetamovie.pstatic.net/libs/1273/1273252/fbc3eff8751aaafbe492_20200122113006690.mp4-pBASE-v0-f97976-20200122113032271_1.mp4"

savePath="D:/gms/Atom/movie.avi"


f=dw.urlopen(moveUrl).read()

with open(savePath, 'wb') as savePath:
    savePath.write(f)

print("다운로드완료!")
