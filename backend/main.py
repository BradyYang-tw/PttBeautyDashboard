import common
import datetime
import sqlite3


def main(custom_date=datetime.datetime.today().strftime("%#m/%d")):
    url = "https://www.ptt.cc/bbs/beauty/index.html"
    domain = "https://www.ptt.cc/"
    href_data, last_url = common.get_page_url(url)
    result = []
    while href_data:
        i = href_data[0]
        print(i)
        if i.find("a") and '正妹' in i.find("a").text:
            date = i.find('div', {'class': 'date'}).text.replace(' ', '')
            # 只抓當日的發文
            if datetime.datetime.strptime(date, "%m/%d") < datetime.datetime.strptime(custom_date, "%m/%d"):
                break
            data = common.get_more_picture(domain + i.find("a")['href'])

            # 將資料寫進SQLlite
            con = sqlite3.connect('mydatabase.db')
            c = con.cursor()
            query = 'INSERT or ignore INTO ptt_beauty (TITLE,URLS, DATE, HREF) VALUES (?, ?, ?, ?)'
            query_data = [i.find("a").text, str(data), date, domain + i.find("a")['href']]
            c.execute(query, query_data)
            con.commit()
            con.close()


            # result.append({"title": i.find("a").text, "url": data})
        href_data.pop(0)
        if not href_data:
            href_data, last_url = common.get_page_url(domain + last_url)


# if __name__ == "__main__":
#     # main("6/25")
#     main("7/27")