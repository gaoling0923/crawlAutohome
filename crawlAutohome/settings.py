# -*- coding: utf-8 -*-

# Scrapy settings for crawlAutohome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawlAutohome'

SPIDER_MODULES = ['crawlAutohome.spiders']
NEWSPIDER_MODULE = 'crawlAutohome.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawlAutohome (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'crawlAutohome.middlewares.CrawlautohomeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'crawlAutohome.middlewares.JavaScriptMiddleware': 543, #543,  # 键为中间件类的路径，值为中间件的顺序
    # 'crawlAutohome.middlewares.MyCustomDownloaderMiddleware': None,
    # 'crawlAutohome.middlewares.ProxyMiddleware': 100,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#后面的None是指不使用这个pipeline，300是一个优先级，数字越大，优先级越高
ITEM_PIPELINES = {
    # 'crawlAutohome.pipelines.MongoDBPipeline': 300,
    #'crawlAutohome.pipelines.b30bbsPipeline': None,
    'crawlAutohome.pipelines.HBasePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#连接数据库的信息，存到mydb的articles数据集中
MONGODB_HOST='127.0.0.1'
MONGODB_PORT=27017
MONGODB_DBNAME='autohome'
MONGODB_DOCNAME='testdb'
# MONGODB_DOCNAME='bsstitle'
#hbase
HBASE_HOST = '10.8.23.6'
# HBASE_HOST = '192.168.0.95'
HBASE_PORT = 9090
# HBASE_TABLE = 'testdb'
HBASE_TABLE = 'autoHomeBBSTitleInfo'
# HBASE_TABLE = 'nbbstitle'
