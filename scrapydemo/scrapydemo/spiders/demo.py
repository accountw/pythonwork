import scrapy
from scrapydemo.items import ScrapydemoItem
class DemoSpider(scrapy.Spider):
    name = "demo"
    allow_domains=('www.douyu.com')
    start_urls = [
        "https://www.douyu.com/directory/all",
    ]

    def parse(self, response):
        a=response.css('li.layout-Cover-item')

        for b in a:
            item = ScrapydemoItem()
            item['name']=b.css('h2.DyListCover-user::text').extract_first()
            item['hname']=b.css('h3.DyListCover-intro::text').extract_first()
            item['redu']=b.css('span.DyListCover-hot::text').extract_first()
            yield item
        #scrapy crawl demo -o d.csv -s FEED_EXPORT_ENCODING=UTF-8


