import scrapy
from ..items import QuotewebcrawlerItem

class ItemContainer(scrapy.Spider):
    
    name = 'itemcontainer'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self,response):

        items = QuotewebcrawlerItem()
        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            quote = quotes.css(".text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            items['quote'] = quote
            items['author'] = author
            items['tag'] = tag
            
            yield items

