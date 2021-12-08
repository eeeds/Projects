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
        print('-'*50)
        title = response.xpath('//h1/a/text()').get()
        print(f'Title: {title}')
        print('-'*50)

        citas = response.xpath('//span[@class = "text" and @itemprop = "text"]/text()').getall()
        print('Citas: ')
        for cita in citas:
            print(f'- {cita}')
        print('-'*50)

        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        print('Tags:')
        for tag in top_ten_tags:
            print(f'- {tag}')
        print('-'*50)

