# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanTop100Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影图片
    movie_img = scrapy.Field()
    # 电影名字
    movie_name = scrapy.Field()
    # 电影导演
    movie_director = scrapy.Field()
    # 电影类别
    movie_type = scrapy.Field()
    # 电影上映时间
    movie_data = scrapy.Field()
    # 电影评分
    movie_score = scrapy.Field()
    # 电影剧情介绍
    movie_content = scrapy.Field()

