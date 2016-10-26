# -*- coding: utf-8 -*-
import os
from urllib import request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random


# class DulicatesPipelie(object):
#     def __init__(self):
#         self.links = set()
#
#     def process_item(self,item,spider):
#         if item['pic_url'] in self.links:
#             raise DropItem("Duplicate item found: %s" % item)


class DoubanYpySpiderPipeline(object):
    def process_item(self, item, spider):
        # filename = "d:/img/three"+str(random.randint(1,100))+".txt"
        # with open(filename, 'w') as f:
        #     # for na in item['name']:
        #     #     f.write(na)
        #     #     f.write('\t')
        #     # f.write('\n')
        #     # for ma in item['pic_url']:
        #     #     f.write(ma)
        #     f.write(item['name'])
        #     f.write('\t')
        #     f.write(item['pic_url'])
        #     f.write('\n')
        try:
            request.urlretrieve(item['pic_url'], os.path.join('d:/img/', item['name']))
        except:
            print('这张图片不能下载', item['name'], item['pic_url'])
        return item
