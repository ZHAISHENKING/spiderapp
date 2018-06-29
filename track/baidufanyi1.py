import urllib.request

url = 'http://www.baidu.com/'

# 向一个url发送请求会得到一个HTTPResponse对象
# response = urllib.request.urlopen(url)
# print(type(response))
# # response对象的访问
# print(response.getcode())
#
# print(response.geturl())
#
# print(response.read().decode('utf-8'))
# print(response.getheaders())
#
# print(response.readline())
#
# print(response.readlines())

# 使用urlretriev 保存一个网页
# urllib.request.urlretrieve(url,'baidu.html')

img_url = 'http://img4.imgtn.bdimg.com/it/u=2813434517,83142011&fm=200&gp=0.jpg'
urllib.request.urlretrieve(img_url,'love.jpg')

# 视频下载
vedio_url = 'http://vliveachy.tc.qq.com/om.tc.qq.com/Az8VBMvmOaZ0-uMvijuncOt2WA-hjsfSbUUQjtYZv4Oo/j06552sg6he.p712.1.mp4?sdtfrom=v1105&guid=dabdf0bb81db817f535700efd44a086c&vkey=8722EBFA35A66E250EF94BA72CFA5FC0776AAA68D4855DA156731D9A83B1B6CA3B664F810509D918F5BD577EDFB07C612A8F2760966F776A10554826996CB3A0FBBE8EA6B17450FF173DA43B607B14A3DE1EB9B1EF12D93A1526FE7F8D6571B06C534E987D251DAB8B2B2B7F6D903997DD1D8AC267D77FEF&ocid=2603685292&ocid=760288684'

urllib.request.urlretrieve(vedio_url,'vedio.mp4')

# 使用with open进行数据保存
# response = urllib.request.urlopen(img_url)
# content = response.read()
# print(content)
#
# with open('meinv.jpg','wb') as fp:
# 	fp.write(content)

# 保存网页

response = urllib.request.urlopen(url=url)
content = response.read().decode('utf-8')

with open('baidu2.html','w',encoding='utf-8') as fp:
	fp.write(content)
