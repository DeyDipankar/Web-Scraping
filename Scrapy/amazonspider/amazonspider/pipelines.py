# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class AmazonspiderPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(host= 'localhost', port=27017)
        self.db = self.conn['amazon_db']
        self.collections = self.db['amazon_laptops']

    def process_item(self, item, spider):
        self.collections.insert(dict(item))
        return item
