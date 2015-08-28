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
      "NJU": ["nju.edu.cn", "http://www.nju.edu.cn", '(8359\d+)|(8968\d+)'],
      "THU": ["tsinghua.edu.cn", "http://www.tsinghua.edu.cn/publish/newthu/index.html", '(6279\d+)'],
      "BUAA": ["buaa.edu.cn", "http://www.buaa.edu.cn", '(8231\d+)'],
      "PKU": ["pku.edu.cn", "http://www.pku.edu.cn", '(6275\d+)'],
      "HIT": ["hit.edu.cn", "http://www.hit.edu.cn", '(8641\d+)|(8628\d+)'],
      "HUST": ["hust.edu.cn", "http://www.hust.edu.cn", '(8754\d+)|(8369\d+)'],
      "BUPT": ["bupt.edu.cn", "http://www.bupt.edu.cn", '(6228\d+)|(5882\d+)'],
      "WHU": ["whu.edu.cn", "http://www.whu.edu.cn", '(6875\d+)'],
      "USTC": ["ustc.edu.cn", "http://www.ustc.edu.cn", '(6360\d+)'],
      "XIDIAN": ["xidian.edu.cn", "http://www.xidian.edu.cn", '(8189\d+)|(8820\d+)'],
      "XJTU": ["xjtu.edu.cn", "http://www.xjtu.edu.cn", '(8266\d+)|(8265\d+)|(8339\d+)'],
      "NWPU": ["nwpu.edu.cn", "http://www.nwpu.edu.cn", '(8849\d+)'],
      "BIT": ["bit.edu.cn", "http://www.bit.edu.cn", '(6891\d+)|(8138\d+)'],
      "UESTC": ["uestc.edu.cn", "http://uestc.edu.cn", '(8320\d+)'],
      "DLUT": ["dlut.edu.cn", "http://www.dlut.edu.cn", '(8470\d+)'],
      "SCU": ["scu.edu.cn", "http://www.scu.edu.cn", '(8608\d+)|(8540\d+)'],
      "CQU": ["cqu.edu.cn", "http://www.cqu.edu.cn", '(6510\d+)|(6567\d+)|(6510\d+)'],
      "SYSU": ["sysu.edu.cn", "http://www.sysu.edu.cn/2012/cn/index.htm", '(8411\d+)|(8733\d+)'],
      "NJTU": ["njtu.edu.cn", "http://www.njtu.edu.cn", '(5168\d+)'],
      "USTB": ["ustb.edu.cn", "http://www.ustb.edu.cn", '(6233\d+)|(6574\d+)'],
      "CSU": ["csu.edu.cn", "http://www.csu.edu.cn", '(8887\d+)'],
      "NUAA": ["nuaa.edu.cn", "http://www.nuaa.edu.cn/nuaanew/", '(8489\d+)|(5211\d+)'],
      "XMU": ["xmu.edu.cn", "http://www.xmu.edu.cn", '(2186\d+)'],
      "RUC": ["ruc.edu.cn", "http://www.ruc.edu.cn", '(6251\d+)'],
      "NWU": ["nwu.edu.cn", "http://www.nwu.edu.cn", '(8830\d+)|(8837\d+)'],
      "DLMU": ["dlmu.edu.cn", "http://www.dlmu.edu.cn", '(8472\d+)'],
      "NANKAI": ["nankai.edu.cn", "http://www.nankai.edu.cn", '(2350\d+)'],
      "CQUPT": ["cqupt.edu.cn", "http://www.cqupt.edu.cn/cqupt/index.shtml", '(6246\d+)'],
      "NJUPT": ["njupt.edu.cn", "http://www.njupt.edu.cn", '(8586\d+)|(8349\d+)']
    }

    name = "tel"
    allowed_domains = []
    start_urls = []
    rules = (Rule(LinkExtractor(deny = (
      'http://opac\.lib\.sjtu\.edu\.cn/.*','http://ourex\.lib\.sjtu\.edu\.cn/.*', 'http://topics\.sjtu\.edu\.cn/news/.*', 'http://bbs\.sjtu\.edu\.cn/.*', 'https://bbs\.sjtu\.edu\.cn/.*',
      'http://xblk\.ecnu\.edu\.cn/.*',
      'http://news\.fudan\.edu\.cn/.*', 'http://www\.fdsm\.fudan\.edu\.cn/.*',
      'http://bbs\.ecust\.edu\.cn/.*', 'http://news\.ecust\.edu\.cn/.*', 'http://newsadmin\.ecust\.edu\.cn/.*',
      'http://www\.news\.zju\.edu\.cn/.*',
      'http://www\.tsinghua\.edu\.cn/publish/news/.*', 'http://ftc\.lib\.tsinghua\.edu\.cn/.*', 'http://news\.tsinghua\.edu\.cn/.*', 'http://metalib.lib.tsinghua.edu.cn/.*',
      'http://bhxb\.buaa\.edu\.cn/.*',
      'http://bbs\.nwpu\.edu\.cn/.*',
      'http://lib\.ustb\.edu\.cn.*',
      'http://news\.ruc\.edu\.cn/.*'
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

