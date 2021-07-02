1. scrapy startproject amazonspider
2. scrapy genspider amazon_spider amazon.com (create the spider.py)

## Bypassing the user agent
User agent is basicall the browser information that amazon checks in order to get access to scrape their data.

In order to get access for scraping their data, we can either -

        i. either  use GoogleBot(bot deployed by Google to show amzon's products on google search engine).
            when we deploy it like 
                USER_AGENT = "https://developers.whatismybrowser.com/useragents/parse/79googlebot"
            (google - Googlebot User Agents and copy the first link), amzon thinks that google is scraping their sites,not any external agent. source - https://developers.whatismybrowser.com/useragents/explore/software_name/googlebot/
        
        ii. Using scrapy's user-agent. pip install scrapy-user-agents. Then

            DOWNLOADER_MIDDLEWARES = {
            'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
            }

            simply paste it to settings.py

        iii. Using proxy(source - https://github.com/rejoiceinhope/scrapy-proxy-pool). pip install scrapy-proxy-pool> sttings.py add PROXY_POOL_ENABLED = True and then add midddleware

            DOWNLOADER_MIDDLEWARES = {
            # ...
            'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
            'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
            # ...
}