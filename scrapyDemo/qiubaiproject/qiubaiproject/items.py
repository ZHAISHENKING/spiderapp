# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiprojectItem(scrapy.Item):
    # 统一了spider和管道之间数据格式的问题
    # 只关注业务逻辑,要保存什么数据，就要创建什么属性，属性的创建方法是统一的
    name = scrapy.Field()
    age = scrapy.Field()
    img_url = scrapy.Field()