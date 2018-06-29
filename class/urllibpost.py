from urllib import request
import urllib.parse

url = 'http://10.31.161.89:8000/users/'
values = {
    "username":"shire",
    "password":"qianfeng",
    "mobile":"15129087058"
}

# 对数据进行编码
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = request.Request(url, data=data)
request.urlopen(req)