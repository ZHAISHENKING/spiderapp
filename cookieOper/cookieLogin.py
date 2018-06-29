from http import cookiejar
import requests
from urllib import request

url = 'http://zskin.xin/admin/'
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}


def save_cookie():

    cookie = cookiejar.MozillaCookieJar('cookie.txt')
    cookie_processor = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_processor)
    response = opener.open(url)
    cookie.save()


def cookie_login():

    cookie = cookiejar.MozillaCookieJar()
    cookie.load('cookie.txt')
    r = requests.get(url, cookies=cookie)
    print(r.content)