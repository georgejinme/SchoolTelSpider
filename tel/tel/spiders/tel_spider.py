import scrapy
from tel.items import TelItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class telSpider(CrawlSpider):

    school = ""
    schoolDic = {
      "SJTU": ["sjtu.edu.cn", "http://www.sjtu.edu.cn", '(5474\d+)|(3420\d+)'],
      "ECNU": ["ecnu.edu.cn", "http://www.ecnu.edu.cn", '(6223\d+)|(5434\d+)'],
      "FDU": ["fudan.edu.cn", "http://www.fudan.edu.cn", '(6564\d+)'],
      "SHU": ["shu.edu.cn", "http://www.shu.edu.cn/IndexPage.html", '(9692\d+)|(5633\d+)'],
      "ECUST": ["ecust.edu.cn", "http://www.ecust.edu.cn", '(6425\d+)|(3361\d+)'],
      "TJU": ["tongji.edu.cn", "http://www.tongji.edu.cn", '(6598\d+)|(6598\d+)'],
      "SISU": ["shisu.edu.cn", "http://www.shisu.edu.cn", '(6770\d+)|(3537\d+)'],
      "SHUFE": ["shufe.edu.cn", "http://www.shufe.edu.cn/structure/index", '(6590\d+)'],
      "ZJU": ["zju.edu.cn", "http://www.zju.edu.cn", '(8820\d+)|(8795\d+)'],
      "NJU": ["nju.edu.cn", "http://www.nju.edu.cn", '(8359\d+)|(8968\d+)']
    }

    name = "tel"
    allowed_domains = []
    start_urls = []
    rules = (Rule(LinkExtractor(deny = (
      'http://opac\.lib\.sjtu\.edu\.cn/.*','http://ourex\.lib\.sjtu\.edu\.cn/.*', 'http://topics\.sjtu\.edu\.cn/news/.*', 'http://bbs\.sjtu\.edu\.cn/.*', 'https://bbs\.sjtu\.edu\.cn/.*',
      'http://xblk\.ecnu\.edu\.cn/.*',
      'http://news\.fudan\.edu\.cn/.*', 'http://www\.fdsm\.fudan\.edu\.cn/.*',
      'http://bbs\.ecust\.edu\.cn/.*', 'http://news\.ecust\.edu\.cn/.*', 'http://newsadmin\.ecust\.edu\.cn/.*',
      'http://www\.news\.zju\.edu\.cn/.*'
    ),), callback = 'parse_item', follow = True),)

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

