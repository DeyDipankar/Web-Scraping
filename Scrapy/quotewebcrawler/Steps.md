1. Install pip
2. pip install virtualenv
3. virtualenv my_env --python=python3.7.3
4. pip install scrapy
5. pip freeze>requirments.txt

----------create a title web crawler---------
1. create a .py file and rename it 'my_crawler'
2. change directory to project name and then run - scrapy crawl <name of the crawler defined inside the class>
Note: for win32 error. pip install pywin32
3. To get the text part only without the tag - response.css("title::text").extract() 
  or response.css("title::text").extract_first() or response.css("title::text")[0].extract() (to get the first element)
  Note: Instead of running the crawler itself we could run this from scrapy shell- scrapy shell "<url to scrape>"

*** Add SelectorGadgetChrome extension to chrome to get the css selectors***

--------------syntaxes----------------------------
css selectors : response.css("span.author::text").extract() or simply (".author:text")
xpath : response.xpath("//span[@class='author']/text()).extract()
combination : response.css("li.next a").xpath("@href").extract()

-------------item container-------------------------
1. create scrapy field variables under the class in items.
2. import the class in .py spider file, create the object and store data in those variables defined under the class
in items.py

-----------to save the scraped data into files--------
Process flow of storing data:-
1. scraped data -> item container -> output file(json,csv etc.)

2. scraped data -> item container -> pipelines -> sql/mongoDB

scrapy crawl somespider -o filename.json/.csv etc.

----------to save the scraped data into a database---------
1. first make sure the item container is done.
2. Go to setttings.py and uncomment the "ITEM_PIPELINES" to activate the pipelines defined in pipelines.py
If you have multiple pipelines classes defined then you need to add all the pipeline classes into that "ITEM_PIPELINES"
list in settings.py
