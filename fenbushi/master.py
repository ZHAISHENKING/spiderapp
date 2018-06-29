
# !/usr/bin/env python
from queue import Queue
import threading
import requests
import re
import redis

start_url = "http://www.geyanw.com"
# 队列,存放要爬取的url
# urls_queue = Queue()
urls_queue = redis.Redis(host='47.104.229.81', port=6379, db=0)
# 并发下载线程数
DOWNLOADER_NUM = 10
# 线程池
thread_pool = []


def fetch(url):
    """
    根据url获取url对应的内容,并从网页中提取要爬取的url。
    把提取的url put 到队列。
    Args：
        url：要下载的页面的地址
    Returns:
        text:网页的内容
    """
    try:
        r = requests.get(url)
        html = r.content
        text = html.decode('gb2312')
        # text = html.decode('ISO-8859-1')
        return text
    except Exception as e:
        print(e)
    else:
        # 检测http返回的状态码是否正常
        r.raise_for_staus()


def parse(html):
    """
    对一级页面进行解析，解析html源码中的内容。
    Args：
        html：网页的源码, html的类型是str。
    """
    pattern = re.compile(r'href="(/[a-z0-9-/]+(.html)?)"')
    urls = pattern.findall(html)
    for url in urls[:5]:
        print(url[0])
        urls_queue.sadd('links', start_url + url[0])
        # urls_queue.put(start_url + url[0])


def parse_detail(html):
    """
    解析详情页中的内容，从详情页中抽取数据。
    Args:
        html:详情页的源代码。
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    print(soup.text)


def downloader():
    """
    从url队列中提取url，下载url对应的页面。
    每个url都是一个详情页的地址。
    Returns:
        None
    """
    # 不停地从url队列中取url，如果url不是None，下载url页面，并进行解析。
    while True:
        # url = urls_queue.get()
        url = urls_queue.spop('links')
        if url is not None:
            print(url)
            html = fetch(url)
            parse_detail(html)


def main():
    """
    在主线程中初始化url队列。
    根据DOWNLOAD_NUM的设置，启动多个线程，多个线程并发地从
    url队列中获取url，执行url页面的下载。
    """
    # 主线程中初始化队列
    html = fetch(start_url)
    parse(html)
    # 启动多个子线程
    for i in range(DOWNLOADER_NUM):
        t = threading.Thread(target=downloader)
        t.start()
        thread_pool.append(t)
    # 阻塞队列，直到队列中没有任何url
    # urls_queue.join()
    # 阻塞线程，直到所有线程结束
    for t in thread_pool:
        t.join()


if __name__ == '__main__':
    main()
