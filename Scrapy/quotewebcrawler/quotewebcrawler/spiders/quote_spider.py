import scrapy

class quotespider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        title = response.css('title::text').extract() #note the syntax "title::text"
        yield ({'title_txt':title})