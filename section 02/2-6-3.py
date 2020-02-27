from bs4 import BeautifulSoup
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

fp = open("D:/Atom/section 02/car.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

# print(soup)

def car_func(selector) :
    print("car_func : ", soup.select_one(selector).string)

car_lambda=lambda q: print("car_lambda : ", soup.select_one(q).string)


car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
car_lambda("#cars > #gr")
