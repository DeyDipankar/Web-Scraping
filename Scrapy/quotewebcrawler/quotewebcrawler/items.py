# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotewebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    quote = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    
