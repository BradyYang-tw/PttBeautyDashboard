from bs4 import BeautifulSoup
import requests
import urllib.request
import re # 正規表示
import os # 操作系統資料夾、檔案
from flask import jsonify, Flask
import json

pageURL = "https://www.ptt.cc/bbs/beauty/index.html"
domain = "https://www.ptt.cc/"
res = requests.get(pageURL, cookies={'over18': '1'})
soup = BeautifulSoup(res.text, 'html.parser')
href_data = soup.find_all('div', {'class': "r-ent"})
print(href_data[1])
result = []
while href_data:
# for i in href_data:
    i = href_data[0]
    if i.find("a") and '正妹' in i.find("a").text:
        res2 = requests.get(domain + i.find("a")['href'], cookies={'over18': '1'})
        soup2 = BeautifulSoup(res2.text, 'html.parser')
        result.append({"title": i.find("a").text, "url": soup2.find_all('a', {'class':''})[1]["href"]})
    href_data.pop(0)
if __name__ == "__main__":
    print("Go")
    print(result)
    # print(json.dumps(result, ensure_ascii=False))