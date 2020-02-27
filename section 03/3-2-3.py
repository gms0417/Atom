import requests, json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

s=requests.session()
r=s.get('http://httpbin.org/stream/20')
    # encoding 이 안되어 있으면 None
if r.encoding==None:
    r.encoding='utf-8'
# print(r.encoding)

for line in r.iter_lines(decode_unicode=True):  #인코딩 후 > 디코드하여야 보임
    b = json.loads(line)
    # print(b.keys())
    for e in b.keys() :
        print(e ," : ", b[e])
