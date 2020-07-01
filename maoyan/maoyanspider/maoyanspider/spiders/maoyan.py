import scrapy
from scrapy.selector import Selector
from maoyanspider.items import  MaoyanspiderItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    #设置请求头信息
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        cookies={
            'Cookie':'__mta=247354299.1593180880151.1593182538528.1593231838432.7; uuid_n_v=v1; uuid=5E4ACCC0B7B711EA842AD7B3BE0152F25B962864519D4E94AE7AADF177D9E9CD; _csrf=7ad862939c48ec376622b17dd224276c0e9a1b353d2a1c577f88aee3f201aeaa; mojo-uuid=2c6011b63d436437c90972dd503dc80f; _lxsdk_cuid=172f0fafcf2c8-001b1100cff20b-31617402-1aeaa0-172f0fafcf2c8; _lxsdk=5E4ACCC0B7B711EA842AD7B3BE0152F25B962864519D4E94AE7AADF177D9E9CD; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593181515,1593410601,1593410653,1593411369; mojo-session-id={"id":"8ed69a0b7f7e01ec45e804dae0ad8983","time":1593566249871}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593566290; __mta=247354299.1593180880151.1593231838432.1593566290495.8; _lxsdk_s=17307f343d5-1c1-676-837%7C%7C4'
        }
        yield scrapy.Request(url=url,cookies=cookies,callback=self.parse)
    
    def parse(self, response):
        items=[]
        for film in Selector(response=response).xpath("//div[@class='movie-hover-info']")[:10]:
            item = MaoyanspiderItem()
            titles = film.xpath("./div[1]/span[1]/text()")
            types = film.xpath(".//div[2]/text()[2]")
            time = film.xpath(".//div[4]/text()[2]")

            item['titles'] = titles.extract()[0].strip()
            item['types'] = types.extract()[0].strip()
            item['time'] = time.extract()[0].strip()
            items.append(item)
        return items
            

 


        
    
