import scrapy
from tel.items import TelItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class telSpider(CrawlSpider):
    name = "SJTU"
    allowed_domains = ["sjtu.edu.cn"]
    start_urls = [
        "http://www.sjtu.edu.cn"
    ]

    rules = (
      Rule(LinkExtractor(), callback = 'parse_item', follow = True),
    )


    def parse_item(self, response):
      for sel in response.xpath('//*/text()'):
        tel = sel.re('(5474\d+)|(3420\d+)')
        if tel != []:
          item = TelItem()
          item['name'] = response.xpath('//title/text()').extract()
          item['tel'] = tel
          yield item

