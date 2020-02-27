import sys
import io
import urllib.request
import urllib.parse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

API ="http://api.ipify.org"

values={
'format' : "json"
}


print('before', values)
params=urllib.parse.urlencode(values)
print('after', params)

# 요청 URL 생성
url = API + "?" + params
print("요청 url = ", url)

# 읽기
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)
