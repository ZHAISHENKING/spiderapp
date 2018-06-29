import re
import codecs
with open('geyanw.html', encoding='gbk') as f:
    html = f.read()

print(type(html))

pattern = re.compile(r'href="(/[/\w-]+)')

urls = pattern.findall(html)
print(len(urls))
# for url in urls:
#     print(url)