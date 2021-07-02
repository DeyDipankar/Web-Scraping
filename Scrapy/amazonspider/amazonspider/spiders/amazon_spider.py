import scrapy
from ..items import AmazonspiderItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=laptops&i=electronics-intl-ship&ref=nb_sb_noss']
    page_no = 2
    
    

    def parse(self, response):
        item = AmazonspiderItem()

        product_name = response.css(".a-color-base.a-text-normal").css("::text").extract()
        product_price = response.css(".a-offscreen::text").extract()
        product_imagelink = response.css(".s-image::attr(src)").extract()
        product_total_reviews = response.css(".a-size-small .a-link-normal .a-size-base").css("::text").extract()

        item['product_name'] = product_name
        item['product_price'] = product_price
        item['product_imagelink'] = product_imagelink
        item['product_total_reviews'] = product_total_reviews

        yield item

        next_page = "https://www.amazon.com/s?k=laptops&i=electronics-intl-ship&page=" + str(self.page_no) + "&qid=1625242444&ref=sr_pg_" + str(self.page_no)
        #https://www.amazon.com/s?k=laptops&i=electronics-intl-ship&page=3&qid=1625242608&ref=sr_pg_3
        #https://www.amazon.com/s?k=laptops&i=electronics-intl-ship&page=4&qid=1625242620&ref=sr_pg_4
        if self.page_no <= 3:
            print(self.page_no)
            yield response.follow(next_page, callback = self.parse)
        self.page_no+=1

        

