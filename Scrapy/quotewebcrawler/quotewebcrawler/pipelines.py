# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class QuotewebcrawlerPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        """
            This method will create the database connection & the cusror object
        """
        self.conn = sqlite3.connect("my_db.db")
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        self.cursor.execute(""" DROP TABLE IF EXISTS my_table""")
        self.cursor.execute(""" CREATE TABLE my_table (
                                Quote text,
                                Author text,
                                Tag text)"""
                            )

    def process_item(self, item, spider):
        #print(item['quote'])
        self.store_db(item)
        return item

    def store_db(self,item):
        #pass
        self.cursor.execute(""" INSERT INTO my_table VALUES(?,?,?)""",(item['quote'][0],item['author'][0],
                                                                            item['tag'][0])
                            )
        self.conn.commit()
