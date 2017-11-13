# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class MaoyanTop100Pipeline(object):
    def __init__(self):
        
        """
        初始化主机名,端口号,数据库名.数据表名
        """
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        
        # 创建mongodb数据库链接
        client = pymongo.MongoClient(host=host,port=port)
        # 指定数据库
        mydb =client[dbname]
        # 存放数据库表名
        self.post=mydb[sheetname]

    def process_item(self, item, spider):
        
        # 把类字典类型转成字典类型
        data=dict(item)
        # 把数据插到数据表
        self.post.insert(data)
        return item


