import scrapy
from tel.items import TelItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class telSpider(CrawlSpider):

    school = ""
    schoolDic = {
      "SJTU": ["sjtu.edu.cn", "http://www.sjtu.edu.cn", '(5474\d+)|(3420\d+)']
    }

    name = "tel"
    allowed_domains = []
    start_urls = []
    rules = (Rule(LinkExtractor(), callback = 'parse_item', follow = True),)

    def __init__(self, school=None, *args, **kwargs):
      super(telSpider, self).__init__(*args, **kwargs)
      self.school = school
      self.allowed_domains = [self.schoolDic[self.school][0]]
      self.start_urls = [
        self.schoolDic[self.school][1]
      ]
      


    def parse_item(self, response):
      for sel in response.xpath('//*/text()'):
        tel = sel.re(self.schoolDic[self.school][2])
        if tel != []:
          item = TelItem()
          item['name'] = response.xpath('//title/text()').extract()
          item['tel'] = tel
          yield item

