# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook


class SinamasteranalysisPipeline(object):
    def  __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['title'], ['content'], ['time'], ['userID'], ['url'], ['isVip'])
        
    def process_item(self, item, spider):
        line = [item['title'], item['content'], item['time'], item['userID'], item['url'], item['isVip']]
        self.ws.append(line)
        self.wb.save('job.xlsx')
        return item
