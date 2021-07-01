# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class QuotewebcrawlerPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(host='localhost',port=27017)
        self.db = self.conn['quotes_db']
        self.collections = self.db.collection['quotes']

    def process_item(self, item, spider):
        #print(item['quote'])
        self.collections.insert(dict(item))
        return item