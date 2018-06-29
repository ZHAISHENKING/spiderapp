import urllib.parse
import urllib.request
import json

url = 'http://fanyi.baidu.com/?aldtype=16047#en/zh/'

# word = input('请输入要查询的单词')

# url = url+word
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2626.76 Safari/537.36'

}
# response=urllib.request.urlopen(url=url)
#
# content = response.read().decode('utf-8')
# # 对返回的数据解析
# # xpath/正则/BeautifulSoup
# print(content)

post_url = 'http://fanyi.baidu.com/sug'
# 处理post请求, 表单通过data参数进行设置
data = {
    'kw':'baby'
}
# post请求的data数据必须经过urldecode编码
data = urllib.parse.urlencode(data).encode('utf-8')


# 伪装浏览器访问
request = urllib.request.Request(url=post_url,data=data,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

json_str = json.loads(content,encoding='utf-8')

print(json_str)

json.dump(json_str, open('result.json','w',encoding='utf-8'),ensure_ascii=False)