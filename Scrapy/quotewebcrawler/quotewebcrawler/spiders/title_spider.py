import scrapy

class quotespider(scrapy.Spider):
    name = 'titles'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        title = response.css('title::text').extract() #note the syntax "title::text"
        #we can also use response.css('title::text').extract_first() instead of response.css('title::text')[0]
        #to get the first element, difference is extract_first() returns None ifno item is found -this is an advantage
        yield ({'title_txt':title})