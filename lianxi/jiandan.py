# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import hashlib
import re
import base64
import threading


def _md5(value):
    '''md5加密'''
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()


def _base64_decode(data):
    '''bash64解码，要注意原字符串长度报错问题'''
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)


def get_imgurl(m, r='', d=0):
    '''解密获取图片链接'''
    e = "DECODE"
    q = 0
    r = _md5(r)
    o = _md5(r[0:0 + 16])
    n = _md5(r[16:16 + 16])
    l = m[0:q]
    c = o + _md5(o + l)
    m = m[q:]
    k = _base64_decode(m)
    t = str(k)[1:].strip(r"'")
    return t


def get_r(js_url):
    '''获取关键字符串'''
    r = requests.get(js_url)
    r.encoding = "GBK"
    js = r.text
    _r = re.findall('c=[\w\d]+\(e,"(.*?)"\)', js)[0]
    return _r


def load_img(imgurl, file):
    '''下载单张图片到制定的文件夹下'''
    name = imgurl.split('/')[-1]
    file = "{}/{}".format(file,name)
    item = requests.get(imgurl).content
    with open(file,'wb') as f:
        f.write(item)
    print('{} is loaded'.format(name))


def load_imgs(url, file):
    '''多线程下载单页的所有图片'''
    threads = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Host': 'jandan.net'
    }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    # 这个地方必须使用[-1]来提取js地址，因为有的页面有两个js地址，其中第一个是被注释了不用的
    js_url = re.findall('<script src="(//cdn.jandan.net/static/min/[\w\d]+\.\d+\.js)"></script>', html)[-1]
    _r = get_r('http:{}'.format(js_url))
    tags = soup.select('.img-hash')
    for each in tags:
        hash = each.text
        img_url = 'http:' + get_imgurl(hash, _r)
        print(img_url)
        t = threading.Thread(target=load_img, args=(img_url, file))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print(url, 'is ok')


if __name__ == '__main__':
    load_imgs('http://jandan.net/ooxx', '/Users/mac/PycharmProjects/spider/meizi')
