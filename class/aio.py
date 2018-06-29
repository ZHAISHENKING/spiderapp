import asyncio
import re
import aiohttp
from bs4 import BeautifulSoup

# 网站host
HOST = "https://www.geyanw.com/"
start_url = 'https://www.geyanw.com'
# 使用一个list存储已爬取的url队列
crawled_urls = []


# 获取网页内容
async def get_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    html = await response.read()
                    # soup = BeautifulSoup(html, 'lxml')
                    # with open('geyan/'+url[-8:-4]+'.html', 'wb') as f:
                    #     f.write(soup)
                    print(url)
                    return {'error': '', 'html': html}
                else:
                    return {'error': response.status, 'html': ''}
    except Exception as e:
        return {'error': e, 'html': ''}


# 从网页内容中获取关联url
def parse_html(html):
    pattern = re.compile(r'href="(/[a-z0-9-/]+(.html)?)')
    urls = pattern.findall(html.decode('ISO-8859-1'))
    return [start_url+url[0] for url in urls]


async def work(q):
    """
    每次从q队列中取出一个url, 以异步的方式发送一个请求
    队列为空 结束请求
    """
    while not q.empty():
        url = await q.get()
        if not url in crawled_urls:
            crawled_urls.append(url)
        content = await get_content(url)
        if not content['error']:
            urls = parse_html(content['html'])
            for url in urls:
                # url在请求列表中 且 是格言网的url，就爬取该url
                if not url in crawled_urls and start_url in url:
                    q.put_nowait(url)

        else:
            print(content['error'], url)


q = asyncio.Queue()
if __name__ == '__main__':
    q.put_nowait(start_url)
    # 队列q可以被多个对象同时操作
    loop = asyncio.get_event_loop()
    # 使用列表生成器, 创建多个work
    works = [work(q) for id in range(10)]
    loop.run_until_complete(asyncio.wait(works))
    loop.close()
    print(crawled_urls)
    # with open('geyanw.html', 'rb') as f:
    #     html = f.read()
    # crawled_urls = parse_html(html)
    # for url in crawled_urls:
    #     print(url)
