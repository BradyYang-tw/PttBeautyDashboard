from bs4 import BeautifulSoup
import requests


# 取得一個頁面上所有PTT列表的URL
def get_page_url(url):

    res = requests.get(url, cookies={'over18': '1'})
    soup = BeautifulSoup(res.text, 'html.parser')
    # 取得上一篇網址的URL
    last_url = soup.find_all("a", {"class": "btn wide"})[1]['href']
    # 取得所有文章
    href_data = soup.find_all('div', {'class': "r-ent"})[::-1]
    print(href_data)
    return href_data, last_url


# 取得url下所有照片
def get_more_picture(second_url):
    res = requests.get(second_url, cookies={'over18': '1'})
    soup = BeautifulSoup(res.text, 'html.parser')
    img = []
    for i in soup.find_all('img'):
        print(i)
        img.append(i['src'].replace("cache.ptt.cc/c/https/", ""))
    return img


if __name__ == "__main__":
    pageURL = "https://www.ptt.cc/bbs/beauty/index.html"
    get_page_url(pageURL)
    # get_more_picture("https://www.ptt.cc/bbs/Beauty/M.1658415683.A.D4D.html")