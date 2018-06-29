# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 用于运行爬虫的爬虫名称
    name = 'baidu'
    # 允许域名,只能爬取这个域名下的数据
    allowed_domains = ['www.baidu.com']
    # spider文件首次提交给引擎的url
    # 可以有多个url 可手动配置
    start_urls = ['http://www.baidu.com/']

    # 回调配置, 当下载器下载完一个请求对象的数据
    def parse(self, response):
        items = []
        # 解析当前的response数据
        # print(response.text)
        # 返回一个Selector对象列表
        title = response.xpath('//input[@id="su"]/@value')

        # extract、extract_first()方法可以直接对列表提取内容
        # extract_first() 如果被提取的selector列表为空，也不会报错
        name = title.extract()
        name1 = title.extract_first()
        print(name,name1)
        # 如果不写返回值不会报错, 但无法使用管道
        return items
