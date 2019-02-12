import scrapy

class TermSpider(scrapy.Spider):
    name = 'TermCheck'
    allowed_domains = ['google.com']

    def start_requests(self):
        with open('urls.csv', 'r', encoding='utf8') as file:
            for line in file.readlines():
                yield scrapy.Request(line.strip())
    
    def parse(self, response):
        item = {
            'search_title': response.css('input#sbhost::attr(value)').get(),
            'results': response.css('#resultStats::text').get(),
            'url': response.url,
        }
        yield item