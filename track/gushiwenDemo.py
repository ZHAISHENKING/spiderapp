import requests
from bs4 import BeautifulSoup
from RecognizerFile import Recgonizier

# 请求这个页面，获取验证码图片
login_url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
# 处理登录
post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

s = requests.Session()
response = s.get(login_url,headers=headers)
response.encoding='utf-8'

soup = BeautifulSoup(response.text,'lxml')
img_url = 'https://so.gushiwen.org' + soup.select('#imgCode')[0].attrs.get('src')

# 注意要使用绘画请求图片
img_response = s.get(img_url)
with open('getCode.jpg','wb') as fp:
	fp.write(img_response.content)

r = Recgonizier()
code = r.esay_recognition('getCode.jpg')
print('验证码识别结果'+str(code))


a = soup.select('#__VIEWSTATE')[0].attrs.get('value')
b = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

print(a,b)
data = {
	'__VIEWSTATE': a,
	'__VIEWSTATEGENERATOR': b,
	'from': 'http://so.gushiwen.org/user/collect.aspx',
	'email': '965224116@qq.com',
	'pwd': '123457abc',
	'code': code,
	'denglu': '登录'
}

response = s.post(url=post_url,data=data,headers=headers)
response.encoding='utf-8'
with open('gushi.html','w',encoding='utf-8') as fp:
	fp.write(response.text)


