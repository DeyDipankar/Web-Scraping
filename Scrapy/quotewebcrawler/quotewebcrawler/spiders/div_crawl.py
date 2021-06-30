import scrapy

class DivCrawl(scrapy.Spider):
    name = "divcrawl"
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self,response):
        all_quotes = response.css("div.quote")
        for quotes in all_quotes:
            quote = quotes.css(".text::text").extract()
            author = quotes.css(".author::text").extract()
            tags = quotes.css(".tag::text").extract()
            yield {"quote":quote,
                    "author":author,
                    "tags":tags}