import scrapy
from tupian.items import ImagespiderItem

class ImgspiderSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.woyaogexing.com']
    start_urls = ['https://www.woyaogexing.com/tupian/dongman/',
                  'https://www.woyaogexing.com/tupian/dongman/index_2.html',
                  'https://www.woyaogexing.com/tupian/dongman/index_3.html']

    def parse(self, response):
        a=response.css('img::attr(src)').extract()
        for b in a:
            item = ImagespiderItem()
            front_image_url = [b if 'http:' in b else ('http:' + b)]
            item['imgurl'] = front_image_url
            yield item
        pass
