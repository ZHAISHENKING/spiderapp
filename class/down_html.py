import requests
import threading
from bs4 import BeautifulSoup

"""
爬取文本放入html文件
"""
# url = 'https://www.geyanw.com'
# r = requests.get(url)
# with open('geyanw.html', 'wb') as f:
#     f.write(r.content)

# 读取内容并遍历输出
home_page = "https://www.geyanw.com/"
with open('geyanw.html','rb') as f:
    html_doc = f.read()

urls = []

soup = BeautifulSoup(html_doc,"lxml")
tboxs = soup.find_all(name='dl', class_='tbox')
for tbox in tboxs:
    li_list = tbox.find_all('li')
    for li in li_list:
        urls.append(home_page + li.a.get("href"))
        # print(li.text)


# 获取二级页面内容
r = requests.get(urls[0])
soup = BeautifulSoup(r.content, 'lxml')
content = soup.find(name='div', class_='content').get_text()
print(content)
