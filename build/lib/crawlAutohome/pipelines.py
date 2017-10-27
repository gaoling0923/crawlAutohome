# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import random
from _md5 import md5

import happybase
from scrapy.exceptions import DropItem

from crawlAutohome.items import Qicheluntan, QicheluntanDetail
import pymongo
from scrapy.conf import settings

class randomRowKey(object):
    # 生产唯一key
    def getRowKey(self):
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
        randomNum = random.randint(0, 100)  # 生成的随机整数n，其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        return uniqueNum

class HBasePipeline(object):
    def __init__(self):
        self.host = settings['HBASE_HOST']
        self.table_name = settings['HBASE_TABLE']
        self.port = settings['HBASE_PORT']
        self.connection = happybase.Connection(host=self.host, port=self.port, autoconnect=False)
        # self.connection = happybase.Connection(host=self.host,port=self.port)
        # self.table = self.connection.table(self.table_name)

    def process_item(self, item, spider):
        # cl = dict(item)
        self.connection.open()
        table = self.connection.table(self.table_name)
        # cl = dict(item)
        randomrkey = randomRowKey()
        rowkey = randomrkey.getRowKey()

        if isinstance(item, Qicheluntan):
            # self.table.put('text', cl)
            print('进入pipline')
            title = item['title']
            fromurl = item['fromurl']
            author = item['author']
            titleurl = item['titleurl']
            bbsdate = item['bbsdate']
            replycount = item['replycount']
            liulancount = item['liulancount']
            luntanName = item['luntanName']
            replyperson = item['replyperson']
            replydate = item['replydate']
            crawldate = item['crawldate']
            # item.get('crawldate','')

            table.put(md5(str(rowkey).encode('utf-8')).hexdigest(), {'cf1:title': title,
                                                                      'cf1:fromurl': fromurl,
                                                                      'cf1:author': author,
                                                                      'cf1:titleurl': titleurl,
                                                                      'cf1:bbsdate': bbsdate,
                                                                      'cf1:replycount': replycount,
                                                                      'cf1:liulancount': liulancount,
                                                                      'cf1:luntanName': luntanName,
                                                                      'cf1:replyperson': replyperson,
                                                                      'cf1:replydate': replydate,
                                                                      'cf1:crawldate': crawldate})

        return item


class MongoDBPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        cl = dict(item)
        self.post.insert(cl)
        return item

class CrawlautohomePipeline(object):
    def process_item(self, item, spider):
        return item


class b30bbsPipeline(object):
    def __init__(self):
        self.limit = 50
        self.file = open('D:/crawlfiles/yiqib30/b30.txt', 'wb');
        #self.filedetail = open('D:/crawlfiles/yiqib30/b30_detail.txt', 'wb');



    def process_item(self, item, spider):
        vaild = True
        if item is not None:
            if isinstance(item,Qicheluntan):


                line = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (item['title'],
                                                     item['author'],
                                                     item['url'],
                                                     item['bbsdate'],
                                                     item['replycount'],
                                                     item['liulancount'],
                                                     item['replyperson'],
                                                     item['replydate'])
                self.file.write(line.encode("utf-8"))
                return item
            elif isinstance(item,QicheluntanDetail) :
                print('execute open file')

                line = "%s\t%s\n" % (item['title'])
                self.filedetail.write(line.encode("utf-8"))
                return item
            else :
                raise DropItem("Error")
        else :
            item
