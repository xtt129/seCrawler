# seCrawler(Search Engine Crawler)
A scrapy project can crawl search result of Google/Bing/Baidu

## prerequisite
python 2.7 and scrapy is needed.


## commands

get 50 pages result from search engine with keyword.

say keyword is Spider-Man:

###Bing
scrapy crawl keywordSpider -a keyword=Spider-Man -a se=bing -a pages=10

###Baidu
scrapy crawl keywordSpider -a keyword=Spider-Man -a se=bing -a pages=10

###Google
scrapy crawl keywordSpider -a keyword=Spider-Man -a se=bing -a pages=10


a file urls.txt would be generated under the current directory.



## limitation
it's a tool for collecting links of the search result of the search engine.
it doesn't provide any workaround to the anti-spider measure like CAPTCHA, IP ban list, etc. 
according to my test, Google set the most higher bar for spider to crawl its search result.

