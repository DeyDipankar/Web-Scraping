import scrapy
from ..items import AmazonspiderItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=laptops&i=electronics-intl-ship&ref=nb_sb_noss']
    
    

    def parse(self, response):
        item = AmazonspiderItem()
        #all_divs = response.css(".s-main-slot s-result-list s-search-results sg-row")
        
        # for div in all_divs:
        product_name = response.css(".a-color-base.a-text-normal").css("::text").extract()
        product_price = response.css(".a-offscreen::text").extract()
        product_imagelink = response.css(".s-image::attr(src)").extract()

        item['product_name'] = product_name
        item['product_price'] = product_price
        item['product_imagelink'] = product_imagelink

        yield item

        

