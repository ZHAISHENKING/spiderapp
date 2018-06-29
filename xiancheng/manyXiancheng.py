import requests
import re
import threading
import redis
from queue import Queue


start_url = "http://www.geyanw.com"

# urls_queue = Queue()
urls_queue = redis.Redis(host='localhost', port=6379, db=0)
DOWNLOAD_NUM = 10
# 线程池
thread_pool = []


def fetch(url):
    """
    根据url获取url对应内容 并从网页中提取要爬的url
    把提取的url put 到队列
    Args:
        url: 要下载的页面地址
    Returns:
        text: 网页内容
    """
    r = requests.get(url)
    html = r.content
    try:
        text = html.decode('gb2312')
    except Exception as e:
        text = html.decode('ISO-8859-1')
        print(e)
    return text


def parse(html):
    """
    对一级页面进行解析, 解析html源码中内容
    Args:
        html: 网页源代码
    """
    pattern = re.compile(r'href="(/[a-z0-9-/]+(.html)?)')
    urls = pattern.findall(html)
    for url in urls[:5]:
        urls_queue.sadd('links', start_url + url[0])


def parse_detail(html):
    """
    解析详情页中的内容, 从详情页中获取内容
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)


def downloader():
    """
    从url队列中提取url. 下载url对应的页面
    """
    while True:
        # url = urls_queue.get()
        url = urls_queue.spop('links')
        if url is not None:
            html = fetch(url)
            parse_detail(html)
            # 通知队列刚才取出的url任务下载完成
            # urls_queue.task_done()
            # print('还胜{}个任务未完成'.format(urls_queue.qsize()))


def main():
    """
    在主线程中初始化url队列
    根据download_num的设置, 启动多个线程,
    多个线程并发地从url队列中获取url，执行url页面的下载
    """
    # 主线程中初始化队列
    html = fetch(start_url)
    parse(html)

    # 启动多个子线程
    for i in range(DOWNLOAD_NUM):
        t = threading.Thread(target=downloader)
        t.start()
        thread_pool.append(t)

    # 阻塞队列 直到队列中没有任何url
    # urls_queue.join()

    # 阻塞线程,直到所有线程结束
    for t in thread_pool:
        t.join()


if __name__ == '__main__':
    main()