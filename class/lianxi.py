from bs4 import BeautifulSoup

html = """
<!Doctype html>
<html>
<head>
<meta charset="utf-8">
<title>中华小当家</title>
</head>
<body>
    <div class="aaa" style="background:#ccc;width:20px;height:20px" >
        <p>asdasdasd</p>
        <a href="#>link</a>
        aaa
    </div>
        
</body>
</html>
"""
soup = BeautifulSoup(html, 'lxml')
# 1. 按标签查找元素
print(soup.title)

# 2. 获取子级元素
print(soup.div.p)

# 3. 获取元素文本
print(soup.div.string)

# 4. 获取tag的属性值
print(soup.div.get('class'))
# 返回字典
print(soup.div.attrs)

# 5.find_all和findAll功能完全相同
"""
1 获取所有符合条件的网页元素
2 条件过滤可以是多条件
3 条件过滤可以使用正则表达式
find_all(name, attrs, recursive, text, limit)

text: 按tag内容查找
kwargs: 关键参数
recursive： 是否递归
attrs: 属性过滤
name: 标签名
class_: 类名
"""
print(soup.find_all(name='div', class_='aaa'))