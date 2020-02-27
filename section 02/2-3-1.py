import sys
import io
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

url="http://www.encar.com/"


mem=urllib.request.urlopen(url)
print(type(mem))
print("geturl : ",mem.geturl())
print("status : ",mem.status)

print('headers : ',mem.getheaders())
print('info : ',mem.info())
print("getcode : ",mem.getcode())
print("read : ",mem.read(10))
