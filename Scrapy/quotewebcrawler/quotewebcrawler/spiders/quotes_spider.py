import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    '''def parse(self,response):
        result = response.css(".text::text").extract() #html element 'span' and class = text, so span.text
        yield ({"all_quotes":result})'''

    def parse(self,response):
        result = response.xpath("//span[@class='text']/text()").extract() #html element 'span' and class = text, so span.text
        yield ({"all_quotes":result})