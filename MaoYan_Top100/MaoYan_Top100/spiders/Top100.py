# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from MaoYan_Top100.items import MaoyanTop100Item


class Top100Spider(CrawlSpider):
    name = 'Top100'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4?offset=']

    rules = (
        Rule(LinkExtractor(allow=r"board/4")),
        Rule(LinkExtractor(allow=r'films/\d+'), callback='parse_item'),
    )

    def parse_item(self, response):

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item = MaoyanTop100Item()

        item['movie_img']=response.xpath('//div[@class="avatar-shadow"]/img/@src').extract_first()
        item['movie_name'] = response.xpath('//div[@class="movie-brief-container"]/h3/text()').extract_first()
        item['movie_director'] = response.xpath('//div[@class="celebrity-group"]//div[@class="info"]/a[@class="name"]/text()').extract_first()
        item['movie_type'] = response.xpath('//div[@class="movie-brief-container"]/ul/li[1]/text()').extract_first()
        item['movie_data'] = response.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()').extract_first()
        item['movie_score'] = response.xpath('//div[@class="movie-index-content score normal-score"]/span/span/text()').extract_first()
        item['movie_content'] = response.xpath('//div[@class="mod-content"]/span/text()').extract_first()
        yield item

