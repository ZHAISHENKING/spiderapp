from lxml import etree
#
# with open('../test.html') as f:
#     html_doc = f.read()

# 创建一个element tree
# tree = etree.HTML(html_doc)
#
# print(type(tree))
#
# title = tree.xpath('//html/head/title/text()')
# print(title)
# title_css = tree.cssselect('html > head > title')
# print(title_css[0].text)
url = 'http://sou.zhaopin.com/jobs/searchresult.ashx'
xpath_str = '//*[@id="newlist_list_content_table"]/table'
import requests

r = requests.get(url)
html_doc = r.content
zhaopin = etree.HTML(html_doc)
print(zhaopin)
