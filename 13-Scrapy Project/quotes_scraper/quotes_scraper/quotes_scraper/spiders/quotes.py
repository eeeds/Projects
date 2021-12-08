import scrapy

#Titulo = //h1/a/text()
#Citas = //span[@class = "text" and @itemprop = "text"]/text()
#Top ten tags= //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class = "text" and @itemprop = "text"]/text()').getall()
        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()


        yield {'Title': title, 
                'Citas': quotes, 
                'Top ten tags': top_ten_tags}

