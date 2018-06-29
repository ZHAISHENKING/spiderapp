# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
# 管道就是一个对象，由piplines里面的类进行声明
# piplines里面可以声明多个管道类，每一个管道类可以负责处理一个业务逻辑
# 使用管道之前，必须进行settings里面的设置ITEM_PIPLINS


class QiubaiprojectPipeline(object):

    # 蜘蛛开始爬取的时候自动调用
    def open_spider(self, spider):
        self.fp = open('qiubai.json','w',encoding='utf-8')

    def close_spider(self, spider):
        self.fp.close()

    # 这是一个回调方法，是由引擎自动调用，引擎会把要存储的数据一个一个的通过item参数传递回来
    # spider就是回传数据给引擎的那个蜘蛛对象
    def process_item(self, item, spider):
        json_str = json.dumps(item,ensure_ascii=False)
        self.fp.write(json_str+'\n')
        return item
