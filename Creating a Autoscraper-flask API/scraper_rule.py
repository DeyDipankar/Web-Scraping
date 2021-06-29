from autoscraper import AutoScraper

scraper = AutoScraper()
url = "https://www.flipkart.com/search?q=iphone"
wanted_list = ["APPLE iPhone SE (Black, 64 GB)",
                 "₹49,999"
            ]

result = scraper.build(url,wanted_list)
final_result = scraper.get_result_similar(url,grouped= True)
l= [key for key in final_result.keys()]
scraper.set_rule_aliases({l[0]:'Title', l[2]:'Price'})
scraper.keep_rules(['rule_2i11','rule_h84g'])
scraper.save('title&prices')
