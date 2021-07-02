import scrapy
from scrapy.http import FormRequest
from ..items import QuotewebcrawlerItem

class QuoteScraper(scrapy.Spider):
    name = 'quotescraper'
    start_urls = [
        "http://quotes.toscrape.com/login"
    ]
    #csrf_token = "fPrhmZebSpYAkDsGWxqgiIzyuOVaNRQCEjLKTnUoJHwvBdXFctlM"

    def parse(self,response):
        token = response.css("form input::attr(value)").extract()
        return FormRequest.from_response(response, formdata = {
            "csrf_token" : token,
            "username" : "deydipankar826",
            "password" : "P@ss1234"},
            callback = self.start_scraping
        )

    def start_scraping(self,response):
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
        

