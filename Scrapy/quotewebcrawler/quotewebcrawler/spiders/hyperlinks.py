import scrapy

class HyperLinks(scrapy.Spider):
    name = 'hyperlinks'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self,response):
        result = response.css("a").xpath("@href").extract()
        yield ({"hyperlinks" : result})