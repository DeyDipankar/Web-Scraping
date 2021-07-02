import scrapy
from ..items import QuotewebcrawlerItem

class ItemContainer(scrapy.Spider):
    
    name = 'itemcontainer'
    start_urls = [
        "http://quotes.toscrape.com/page/1/"
    ]
    page_no = 2

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

    ########################## Below codes are used when pagination is there ###########################
        next_page =  'http://quotes.toscrape.com/page/' + str(self.page_no) + '/'  #resturns the next page links such as /page/2/
        print(next_page)
        if self.page_no <= 10:
            yield response.follow(next_page, callback = self.parse)
        self.page_no+=1