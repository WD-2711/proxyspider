from scrapy import Request
from scrapy.spiders import Spider
from proxyspider.items import ProxyspiderItem
from . import check
from tqdm import tqdm

class ProxySpider(Spider):
    name = 'proxyspider'
    index = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    pbar = None

    def start_requests(self):
        url = 'https://www.kuaidaili.com/free/inha/' + str(self.index)
        yield Request(url, headers = self.headers)

    def parse(self, response):
        pageNum = int(self.page)
        if self.index == 1: self.init_pbar(pageNum)
        item = ProxyspiderItem()
        proxys = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        for p in proxys:
            item['ip'] = p.xpath('.//td[@data-title="IP"]/text()').extract()[0]
            item['port'] = p.xpath('.//td[@data-title="PORT"]/text()').extract()[0]
            if check.check(item['ip'], item['port']):
                yield item
        if self.index < pageNum:
            self.pbar.update(1)
            self.index += 1
            next_url = 'https://www.kuaidaili.com/free/inha/' + str(self.index)
            yield Request(next_url, headers=self.headers)
        else:
            self.pbar.close()
            pass
    
    def init_pbar(self, pageNum):
        self.pbar = tqdm(total=pageNum)
