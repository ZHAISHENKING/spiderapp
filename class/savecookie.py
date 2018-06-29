from urllib import request
from http import cookiejar


def save_cookie():

    cookie = cookiejar.MozillaCookieJar('cookie.txt')
    cookie_processor = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_processor)
    response = opener.open('http://www.lagou.com/')
    print(cookie)
    cookie.save()


if __name__ == '__main__':
    save_cookie()
    cookie = cookiejar.MozillaCookieJar()
    cookie.load('cookie.txt')
    for item in cookie:
        print(item)