# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class QuotewebcrawlerPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()
        #self.dump_database()

    def create_connection(self):
        """
            This method will create the database connection & the cusror object
        """
        self.conn = mysql.connector.connect(host = 'localhost',
                                            user = 'root',
                                            passwd = 'P@ss1234',
                                            database = 'itemcontainer'
                                        )
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
        """
            This method is used to write the scraped data from item container into the database
        """
        #pass
        self.cursor.execute(""" INSERT INTO my_table VALUES(%s,%s,%s)""",(item['quote'][0],item['author'][0],
                                                                            item['tag'][0])
                            )
        self.conn.commit()
        #self.dump_database()

    # def dump_database(self):
    #     self.cursor.execute("""USE itemcontainer;SELECT * from my_table INTO OUTFILE 'quotes.txt'""",
    #                         multi = True
    #     )
    #     print("Data saved to output file")
