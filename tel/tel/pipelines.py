# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

import codecs

class TelPipeline(object):
	history = []

	def __init__(self):
		self.file = codecs.open('items.json', 'w', encoding = 'utf-8')

	def process_item(self,item,spider):
		if len(item['tel']) > 0:
			for i in range(len(item['tel']) - 1, -1, -1):
				if not item['tel'][i]:
					item['tel'].pop(i)
			if not (item in self.history):
				self.history.append(item)
				line = json.dumps(dict(item)) + "\n"
				self.file.write(line.decode('unicode_escape'))
				return item

