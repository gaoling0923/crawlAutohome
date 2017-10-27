# -*- coding: utf-8 -*-
import datetime

import re
import scrapy
import time
import requests
from bs4 import BeautifulSoup

from crawlAutohome.items import Qicheluntan


class Spiderb30bbsSpider(scrapy.Spider):
    name = 'spiderbbs'
    allowed_domains = ['club.autohome.com.cn']

    # conn = RedisClient()
    # proxy = conn.pop();
    # proxy = random.choice(PROXIES)
    # if proxy['user_pass'] is not None:
    # request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
    # request.meta['proxy'] = "http://%s" % proxy

    start_urls = [
        # 'http://club.autohome.com.cn/bbs/forum-c-3695-1.html',#奔腾B30论坛
        # 'http://club.autohome.com.cn/bbs/forum-c-632-1.html', #奔腾B50论坛
        # 'http://club.autohome.com.cn/bbs/forum-c-466-1.html',#奔腾B70论坛
        # 'http://club.autohome.com.cn/bbs/forum-c-2310-1.html',#奔腾B90论坛
        # 'http://club.autohome.com.cn/bbs/forum-c-4069-1.html',#奔腾X40论坛
        # 'http://club.autohome.com.cn/bbs/forum-c-3000-1.html',#奔腾X80论坛
        # 'http://club.autohome.com.cn/bbs/forum-c-4117-1.html',#奔腾X4论坛
        # 'http://club.autohome.com.cn/bbs/forum-c-4114-1.html',#奔腾X6论坛
        # 'http://club.autohome.com.cn/bbs/forum-c-3579-1.html'#奔腾X70论坛
        'http://club.autohome.com.cn/bbs/forum-c-4166-1.html',# 宝骏510
        # 'http://club.autohome.com.cn/bbs/forum-c-4166-1.html',# 宝骏510第一页开始
        # 'http://club.autohome.com.cn/bbs/forum-c-3824-1.html',# 森雅R7
        # 'http://club.autohome.com.cn/bbs/forum-c-3080-1.html',# 瑞风S3
        # 'http://club.autohome.com.cn/bbs/forum-c-2778-1.html'# 长安CS35
        # 'http://club.autohome.com.cn/bbs/forum-c-3000-213.html?qaType=-1#pvareaid=101061'
                  ]
    baseurl='http://club.autohome.com.cn/bbs/';




    def __init__(self, **kwargs):
        self.count = 0;

    def parse(self, response):
        self.count=self.count+1;
        print('页数', self.count);
        # scrapy.loging.INFO("进入解析", level=scrapy.loging.INFO)
        coments=response.css('.list_dl')
        #print(coments);

        for sub in coments:

            item = Qicheluntan();
            #print(coments.css('.a_topic::text').extract_first());
            #log.INFO("title 数量："+count, level=log.INFO)
            #print("标题：",sub.css('.a_topic::text').extract_first());

            title= sub.css('.a_topic::text').extract_first();
            fromurl = response.url
            author = sub.css('.linkblack::text').extract_first();
            detailurl = sub.css('.a_topic::attr(href)').extract_first();
            titleurl = response.urljoin(detailurl);
            bbsdate = sub.css('dd .tdate::text').extract_first();
            print('bbsdate2==', bbsdate)
            # bbsdate = sub.css('dd span::text').extract_first();
            # bbsdate = sub.css('dl/dd/span').extract_first();
            # print(bbsdate)
            replycount = sub.css('.list_dl .cli_dd .fontblue::text').extract_first();
            liulancount = sub.css('.list_dl .cli_dd .tcount::text').extract_first();
            luntanName = response.css('body  div.content  div.area.areah div.clubinfo  div.cbinfo h1::text').extract_first();
##subcontent  dl:nth-child(6)  dd:nth-child(2)  a
            item['title']=title.strip() if title  else '' ;
            item['fromurl']=fromurl.strip() if fromurl  else '';
            item['author'] =author.strip() if author  else '';
            #detailurl=sub.css('.a_topic::attr(href)').extract_first();
            item['titleurl'] =titleurl.strip() if titleurl  else ''
            item['bbsdate'] = bbsdate if bbsdate  else ''
            item['replycount'] = replycount.strip() if replycount  else ''
            item['liulancount'] = liulancount.strip() if liulancount  else ''
            item['luntanName'] = luntanName.strip() if luntanName  else ''

            persson=sub.css('.linkblack::text').extract();
            #print('uuu',persson);
            #item['author'] =persson[0];
            if len(persson) <2:

                item['replyperson'] = '';
            else:
                item['replyperson'] = persson[1];
            item['replydate'] = sub.css('.ttime::text').extract_first();

            timeStamp=time.time()
            timeArray = time.localtime(timeStamp)
            nowTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

            item['crawldate']=nowTime

            print('bbsdate2==',bbsdate)

            d1 = datetime.datetime.now()
            d2 = d1 - datetime.timedelta(days=1)

            bbsdate2=bbsdate if bbsdate else d2.date().strftime("%Y-%m-%d")

            fabudate= datetime.datetime.strptime(bbsdate2, "%Y-%m-%d")


            # if fabudate.date() >= d2.date():
            #     yield item
            yield item
        # next = response.css('.afpage::attr(href)').extract_first()
        # nurl=next.strip() if next  else '';
        # url = response.urljoin(nurl);
        # #print('下一页', url);
        # print('页数', self.count);
        # self._wait()
        # yield scrapy.Request(url=url, callback=self.parse);
        soup = BeautifulSoup(response.text, 'lxml')
        gopage= soup.find('span',class_='gopage').find('span').get_text(strip=True)


        # try: / 474 页
        totalpage = gopage[2:-2]
        url=response.url
        # replace str to >> -{{page}}.html
        p = re.compile('(-)\d+(.html$)')
        repl_url = re.sub(p, '\\1{{page}}\\2', url)

        # 接下来要爬取的URLs
        next_urls = [repl_url.replace('{{page}}', str(i)) for i in range(2, int(totalpage) + 1)]
        for next_url in next_urls:
            # self._wait()
            request = scrapy.Request(next_url, callback=self.parse)
            # request.meta['isjs'] = 'False'
            yield request
    def _wait(self):
        for i in range(0, 3):
            print('.' * (i % 3 + 1))
            time.sleep(1)


