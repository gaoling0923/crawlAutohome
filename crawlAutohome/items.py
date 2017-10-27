# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst



class CrawlautohomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class koubeiItem(scrapy.Item):
    buycarline = scrapy.Field()
    carpingfen = scrapy.Field()
    personcount=scrapy.Field()
class koubeiDetailItem(scrapy.Item):
    bugcarline = scrapy.Field()
    buyaddress = scrapy.Field()
    buyjxs = scrapy.Field()
    buydate=scrapy.Field()

class Qicheluntan(scrapy.Item):
    luntanName = scrapy.Field()
    title = scrapy.Field()
    fromurl = scrapy.Field()
    author = scrapy.Field()
    crawldate = scrapy.Field()
    titleurl= scrapy.Field()
    bbsdate=scrapy.Field()
    replycount = scrapy.Field()
    liulancount=scrapy.Field()
    replyperson = scrapy.Field()
    replydate = scrapy.Field()
class QicheluntanDetail(scrapy.Item):
    title = scrapy.Field() #标题
    author = scrapy.Field() #发帖用户
    url= scrapy.Field() #url
    bbsdate=scrapy.Field() #发帖时间
    replycount = scrapy.Field() #回复数
    liulancount = scrapy.Field()#浏览量
    jinghuadie=scrapy.Field() #精华帖
    fatieliang = scrapy.Field()#发帖量
    zhucedate = scrapy.Field()#注册日期
    useraddress = scrapy.Field()#用户地区
    suoshuzushi = scrapy.Field()#所属组织
    guanzhuche = scrapy.Field()#关注车
    aiche = scrapy.Field()#爱车

class SeriesItem(scrapy.Item):
    series_id = scrapy.Field(
        input_processor=MapCompose(lambda v: v.strip("/")),
        output_processor=TakeFirst()
    )
    series_name = scrapy.Field(output_processor=TakeFirst())

class ModelItem(scrapy.Item):
    model_id = scrapy.Field(
        input_processor=MapCompose(lambda v: v[6:v.find("#")-1]),
        output_processor=TakeFirst()
    )
    model_name = scrapy.Field(output_processor=TakeFirst())
    series_id = scrapy.Field(output_processor=TakeFirst())
