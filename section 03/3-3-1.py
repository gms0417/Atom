import requests, json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")


# r=requests.get('https://api.github.com/events')
# r.raise_for_status()          # raise : 에러시 장애발생코드 출력
# print(r.json())
# print(r.text)
jar=requests.cookies.RequestsCookieJar()
# jar.set('name', 'kim', domain='httpbin.org', path='/cookies')
jar.set('name', 'kim')


# r=requests.get('http://httpbin.org/cookies', cookies=jar)
# r.raise_for_status()
# print(r.text)


# r=requests.get('http://httpbin.org/cookies', timeout=3)
# r.raise_for_status()
# print(r.text)


# Fake Rest : test에 성공하면 메세지로 반환(실제로 처리되지 않음)
# r=requests.post('http://httpbin.org/post', data={'name' : 'kim'}, cookies=jar)
# print(r.text)


payload1 = {'key1' : 'value1', 'key2' : 'value2'}
payload2 = (('key1', 'name1'), ('key2', 'name2'))
r=requests.post('http://httpbin.org/post', data=payload2)
print(r.text)
