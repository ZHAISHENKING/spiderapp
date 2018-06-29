from http import cookiejar
from urllib import request


def get_cookie():
    # 创建实例
    cookie = cookiejar.CookieJar()
    # 创建一个cookie处理器
    cookie_processor = request.HTTPCookieProcessor(cookie)
    """
    创建一个opener
    打开链接 获取保存在cookie中的数据
    """
    opener = request.build_opener(cookie_processor)
    response = opener.open('http://www.lagou.com/')
    return cookie


if __name__ == '__main__':

    res = get_cookie()
    for item in res:
        print(item.name)

    # print(res)