# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class SinaMasterAnalysisItem(Item):
    #stockID = Field()#股票码
    #stockName = Field()#股票名
    title = Field()#标题   
    content = Field()#内容
    time = Field()#时间
    userID = Field() #用户id
    url = Field()#链接
    isVip = Field()
    #num = Field()
    #snum = Field()
