# -*- coding: utf-8 -*-
import random
import re

import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider

from douban_ypy_spider.items import DoubanYpySpiderItem


class YpySpider(scrapy.Spider):
    name = "ypy"
    start_urls = [
        "https://ypy.douban.com/package/1894"
    ]

    def parse(self, response):
        item = DoubanYpySpiderItem()

        title_name = response.xpath('//title/text()').extract()[0].strip()
        title_name=title_name[title_name.index(']')+1:title_name.index('·')]


        count = 1
        for sel1 in response.xpath('//div[@class="pic"]/script[@class="cache-photo"]').extract():
            pattern = re.compile('https://[\w|\W]*__l')

            item['pic_url'] = pattern.findall(sel1)[0]
            item['name'] = title_name + str(count) + '.jpg'
            count = count + 1
            yield item

        for sel in response.xpath('//div[@class="relate-package"]'):
            # for sel in response.xpath('//a[@class="package-item"]'):
            package_url = sel.xpath('./a/@href').extract()
            str_package_url=''
            for pa in package_url:
                str_package_url=str_package_url+pa

            whole_url = 'https://ypy.douban.com' + str_package_url
            yield Request(whole_url, callback=self.parse)
