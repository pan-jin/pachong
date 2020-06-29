import scrapy
from scrapy.selector import Selector
from doubanspider.items import DoubanspiderItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

  
#设置爬取的页面
    def start_requests(self):
        for i in range(0,10):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url,callback=self.parse)


#对爬取的页面进行分析
    def parse(self,response):
        items=[]
        movies = Selector(response=response).xpath("//div[@class='hd']")
        for movie in movies:
            item = DoubanspiderItem()
            title = movie.xpath("./a/span[@class='title'][1]/text()")
            link = movie.xpath("./a/@href")
            title = title.extract_first()
            link = link.extract_first()
            item['title'] = title
            item['link'] = link
            items.append(item)
        print(type(items))
        return items
        
